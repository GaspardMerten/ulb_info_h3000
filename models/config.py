from dataclasses import dataclass
from typing import List

from models.geo import Place

__all__ = ('GlobalConfig',)

@dataclass(slots=True)
class GlobalConfig:
    places: List[Place]
