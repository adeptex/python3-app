import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Pattern


def today() -> str:
    """Returns today's date YYYY-MM-DD"""
    today = datetime.now()
    return f"{today.year}-{today.month:02d}-{today.day:02d}"


def load_json_from_file(filename: str = None) -> Dict:
    """Load JSON data from a file"""
    return json.loads(Path(filename).read_text())


def load_regex(regex: str, flags: Optional[re.RegexFlag] = 0) -> Pattern:
    """Try to compile a regex statement"""
    try:
        return re.compile(regex, flags=flags)

    except re.error:
        raise ValueError(f"Failed compiling RegEx: {regex}")


def printer(obj: object, filepath: Path = None) -> None:
    """Print to file or screen"""
    data = str(obj)

    if filepath:
        filepath = filepath.open("w")

    print(data, file=filepath)
