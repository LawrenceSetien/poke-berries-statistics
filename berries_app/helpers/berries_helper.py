import requests
import aiohttp
import asyncio
from helpers.logger import logging
from collections import Counter

POKE_URL = "https://pokeapi.co/api/v2/berry/"

def get_all_berries() -> dict:
    """
    Get all berries data from the Poke API.
    """
    try:
        response = requests.get(POKE_URL)
        response.raise_for_status()
        message = response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise RuntimeError("Failed to fetch berries data") from e
    except ValueError as e:
        logging.error(f"JSON decoding failed: {e}")
        raise RuntimeError("Failed to decode berries data") from e

    return message

async def fetch_growth_time(session: object, url: str) -> int:
    """
    Fetch the growth time of a berry from the given URL.
    Args:
        session (aiohttp.ClientSession): The aiohttp session to use for making the request.
        url (str): The URL to fetch the berry data from.
    Returns:
        int: The growth time of the berry.
    """

    try:
        async with session.get(url) as response:
            response.raise_for_status()
            message = await response.json()
            return message["growth_time"]
    except aiohttp.ClientError as e:
        logging.error(f"Request failed: {e}")
        raise RuntimeError("Failed to fetch growth time data") from e
    except KeyError as e:
        logging.error(f"Key error: {e}")
        raise RuntimeError("Failed to extract growth time from data") from e
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise RuntimeError("An unexpected error occurred") from e


async def get_growth_times(number_of_berries: int) -> list:
    """
    Fetches the growth times for a specified number of berries from the PokeAPI.
    Args:
        number_of_berries (int): The number of berries to fetch growth times for.
    Returns:
        list: A list of growth times for the specified number of berries.
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, number_of_berries):
            url = POKE_URL + str(i)
            tasks.append(fetch_growth_time(session, url))
        growth_times = await asyncio.gather(*tasks)
        return growth_times


def get_berries_names_and_growth(berries_data: dict) -> dict:
    """
    Extracts the names and growth times of berries from the provided data.
    Args:
        berries_data (dict): A dictionary containing information about berries.
            Expected to have the keys "count" and "results", where "results" is a list of dictionaries
            each containing a "name" key.
    """

    number_of_berries = berries_data["count"]
    berries_names = [berry["name"] for berry in berries_data["results"]]
    growth_times = asyncio.run(get_growth_times(number_of_berries))

    return berries_names, growth_times


def calculate_berries_statistics(berries_names: list, growth_times: list) -> dict:
    """
    Calculate various statistics for a given set of berries.
    Args:
        - "berries_names" (list): List of berry names.
        - "growth_times" (list): List of growth times for the berries.
    """

    min_growth_time = min(growth_times)
    max_growth_time = max(growth_times)
    mean_growth_time = round(sum(growth_times) / len(growth_times), 1)
    variance_growth_time = round(sum((x - mean_growth_time) ** 2 for x in growth_times) / len(growth_times), 1)
    median_growth_time = float(sorted(growth_times)[len(growth_times) // 2])
    frequency_growth_time = Counter(growth_times)

    statistics = {
        "berries_names": berries_names,
        "min_growth_time": min_growth_time,
        "max_growth_time": max_growth_time,
        "mean_growth_time": mean_growth_time,
        "variance_growth_time": variance_growth_time,
        "median_growth_time": median_growth_time,
        "frequency_growth_time": frequency_growth_time
    }

    return statistics


