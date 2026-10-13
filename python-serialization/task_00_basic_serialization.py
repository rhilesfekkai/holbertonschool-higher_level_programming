#!/usr/bin/env python3
"""Serialize and deserialize Python dictionaries using JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON from a file and return the deserialized data."""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
