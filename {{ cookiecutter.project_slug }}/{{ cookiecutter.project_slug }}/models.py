import json
from dataclasses import dataclass, field
from typing import Callable, Dict, List


@dataclass
class Model:
    """Definition"""

    name: str
    flag: Callable = lambda: True
    alist: List[str] = field(default_factory=list)
    adict: Dict[str, str] = field(default_factory=dict)

    def __repr__(self) -> str:
        return json.dumps(list(self.__dict__.values()))
