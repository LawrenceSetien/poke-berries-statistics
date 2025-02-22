import matplotlib.pyplot as plt
from flask import Flask, Response, jsonify
from helpers.berries_helper import (
    get_all_berries,
    get_berries_names_and_growth,
    calculate_berries_statistics,
)
from collections import Counter
from io import BytesIO
from base64 import b64encode


app = Flask(__name__)


# TODO
# 1. [x] Get all the berries
# 2. [x] Get the growth time for each berry
# 3. [x] Calculate the min, median, max, variance, mean and frequency of growth time
# 4. [x] Return the result in the format above
# 5. Test the endpoint


@app.route("/health_check", methods=["GET"])
def health_check():
    """
    Simple endpoint to check if the container is up.

    Testing
    """
    return jsonify("ok")


@app.route("/allBerryStats", methods=["GET"])
def allBerryStats():
    """
    Retrieve and calculate statistics for all berries.
    This function fetches data for all berries, extracts their names and growth information,
    calculates various statistics, and returns the results in JSON format.
    Returns:
        Response: A Flask Response object containing the JSON-encoded statistics of all berries.
    """

    message = get_all_berries()
    berries_names, growth_times = get_berries_names_and_growth(message)
    statistics = calculate_berries_statistics(berries_names, growth_times)

    return jsonify(statistics)


@app.route("/histogram", methods=["GET"])
def histogram():
    """
    Generates a histogram of berry growth times and returns it as an HTML image.
    Returns:
        Response: An HTML response containing the base64-encoded histogram image.
    """

    message = get_all_berries()
    _, growth_times = get_berries_names_and_growth(message)
    frequency_growth_time = Counter(growth_times)

    # Generate histogram
    plt.figure(figsize=(10, 6))
    plt.hist(frequency_growth_time, edgecolor="black")
    plt.title("Berry Growth Time Histogram")
    plt.xlabel("Growth Time [Hours]")
    plt.ylabel("Frequency")

    # Save the plot to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    # Encode the image to base64
    img_base64 = b64encode(img.getvalue()).decode("utf8")

    # Return the image in HTML
    html = f'<img src="data:image/png;base64,{img_base64}" />'
    return Response(html, mimetype="text/html")
