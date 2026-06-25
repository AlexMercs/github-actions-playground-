from flask import Blueprint, jsonify
import logging


main = Blueprint("main", __name__)

# Configure logging
logging.basicConfig(level=logging.INFO)


@main.route("/")
def home():
    logging.info("Home route accessed")
    return "Hello, Flask!", 200


@main.route("/health")
def health():
    logging.info("Health check route accessed")
    return jsonify({"status": "ok"}), 200

