from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health_check', methods=['GET'])
def health_check():
    """
    Simple endpoint to check if the container is up.

    Testing
    """
    return jsonify("ok")


@app.route('/test', methods=['GET'])
def test():
    """
    Testing this changes.
    """
    return jsonify("ok")

