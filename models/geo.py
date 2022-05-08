from dataclasses import dataclass

from typing import Dict, Tuple

__all__ = ('Place', 'DistancesMap')


@dataclass(slots=True)
class Place:
    name: str
    lat: float
    long: float
    money: float

    def __hash__(self):
        return self.name.__hash__()


DistancesMap = Dict[Tuple[Place, Place], float]
