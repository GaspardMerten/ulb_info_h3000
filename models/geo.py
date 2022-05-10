from dataclasses import dataclass

from typing import Dict, Tuple

__all__ = ('Place', 'DistancesMap')


@dataclass(slots=True, unsafe_hash=True)
class Place:
    name: str
    lat: float
    long: float
    money: float

DistancesMap = Dict[Tuple[Place, Place], float]
