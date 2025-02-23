import pytest
import requests
from unittest.mock import patch
from helpers.berries_helper import get_all_berries, get_berries_names_and_growth, calculate_berries_statistics


POKE_URL = "https://pokeapi.co/api/v2/berry/"


def test_get_all_berries_success():
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"count": 2, "results": [{"name": "berry1"}, {"name": "berry2"}]}

        result = get_all_berries()
        assert result == {"count": 2, "results": [{"name": "berry1"}, {"name": "berry2"}]}


def test_get_all_berries_request_exception():
    """
    Test case for get_all_berries function to handle request exceptions.
    """
    with patch('requests.get', side_effect=requests.exceptions.RequestException):
        with pytest.raises(RuntimeError, match="Failed to fetch berries data"):
            get_all_berries()


def test_get_all_berries_value_error():
    """
    Test case for get_all_berries function to handle ValueError.
    """
    with patch('requests.get') as mock_get:
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError

        with pytest.raises(RuntimeError, match="Failed to decode berries data"):
            get_all_berries()


def test_get_berries_names_and_growth():
    """
    This test checks if the function correctly extracts berry names and their growth times
    from the provided berries_data dictionary. It mocks the get_growth_times function to
    return predefined growth times.
    """
    berries_data = {"count": 2, "results": [{"name": "berry1"}, {"name": "berry2"}]}

    with patch('helpers.berries_helper.get_growth_times', return_value=[5, 10]):
        result = get_berries_names_and_growth(berries_data)
        assert result == (["berry1", "berry2"], [5, 10])


def test_calculate_berries_statistics():
    """
    This test verifies that the calculate_berries_statistics function correctly calculates
    the statistics for a given list of berry names and their corresponding growth times.
    """
    berries_names = ["berry1", "berry2"]
    growth_times = [5, 10]
    result = calculate_berries_statistics(berries_names, growth_times)
    expected_result = {
        "berries_names": ["berry1", "berry2"],
        "min_growth_time": 5,
        "max_growth_time": 10,
        "mean_growth_time": 7.5,
        "variance_growth_time": 6.2,
        "median_growth_time": 10.0,
        "frequency_growth_time": {5: 1, 10: 1}
    }

    assert result == expected_result