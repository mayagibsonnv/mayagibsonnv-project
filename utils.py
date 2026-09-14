"""Utility functions."""

import os
import json


def load_config(path: str = "config.json") -> dict:
    """Load configuration from a JSON file."""
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return json.load(f)


def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)
