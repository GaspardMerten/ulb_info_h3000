from dataclasses import dataclass
from typing import List

from models.geo import Place, DistancesMap

__all__ = ('GlobalConfig',)


@dataclass(slots=True)
class GlobalConfig:
    places: List[Place]

    distances_map: DistancesMap

    def get_distance_between(self, place_one: Place, place_two: Place) -> float:
        return self.distances_map[place_one, place_two]
