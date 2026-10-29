#!/usr/bin/env python3
"""Flask API with Basic Authentication and JWT authorization."""

import os

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.environ.get(
    "JWT_SECRET_KEY", "dev-secret-key-change-me"
)

basic_auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("adminpass"),
        "role": "admin",
    },
}


@basic_auth.verify_password
def verify_password(username, password):
    """Verify Basic Auth credentials."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@basic_auth.error_handler
def basic_auth_error(status):
    """Return an unauthorized response."""
    return jsonify({"error": "Unauthorized"}), status


@app.route("/basic-protected", methods=["GET"])
@basic_auth.login_required
def basic_protected():
    """Protected route using Basic Authentication."""
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get("username")
    password = data.get("password")
    user = users.get(username) if isinstance(username, str) else None

    if (
        not user
        or not isinstance(password, str)
        or not check_password_hash(user["password"], password)
    ):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": token}), 200


@jwt.unauthorized_loader
def missing_token(error):
    """Handle missing JWTs."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(error):
    """Handle invalid JWTs."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    """Handle expired JWTs."""
    return jsonify({"error": "Token has expired"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route requiring a valid JWT."""
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Allow access only to administrators."""
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


