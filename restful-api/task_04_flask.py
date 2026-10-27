#!/usr/bin/python3
"""Create a simple REST API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """Return the usernames of all stored users."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user's data or a 404 error."""
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a user after validating the submitted JSON."""
    user_data = request.get_json(silent=True)

    if user_data is None or not isinstance(user_data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
