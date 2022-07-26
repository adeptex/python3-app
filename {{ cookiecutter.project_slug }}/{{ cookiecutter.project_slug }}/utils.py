import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from yaml import safe_load


def today() -> str:
    """Returns today's date YYYY-MM-DD"""
    today = datetime.now()
    return f"{today.year}-{today.month:02d}-{today.day:02d}"


def load_yaml_file(filename: Optional[str] = None) -> Dict:
    """Load configuration file."""
    if not filename:
        return {}  # empty

    logging.info(f"Loading YAML file '{filename}'...")
    return safe_load(open(filename))


def load_json_file(filename: str) -> Dict:
    """Load JSON data from a file."""
    logging.info(f"Loading JSON file '{filename}'...")
    return json.loads(Path(filename).read_text())


def save_json_file(filename: str, data: Any) -> None:
    """Save data to a file."""
    logging.info(f"Saving JSON file '{filename}'")
    Path(filename).write_text(str(data))
