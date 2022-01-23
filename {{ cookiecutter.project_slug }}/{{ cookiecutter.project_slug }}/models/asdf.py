import json
from dataclasses import dataclass
from inspect import getsource
from typing import Callable


@dataclass
class Asdf:
    """Definition"""

    name: str  # Unique identifier
    flag: Callable = lambda: True  # Flag implementation

    def __repr__(self) -> str:
        """Serialize as JSON"""
        return json.dumps({"name": self.name, "flag": getsource(self.flag).strip()}, indent=4)
