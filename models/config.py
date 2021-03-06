from dataclasses import dataclass
from typing import List

from models.geo import Place

__all__ = ("GlobalConfig",)

from models.typedef import DistancesMap


@dataclass(slots=True)
class GlobalConfig:
    places: List[Place]

    distances_map: DistancesMap

    def get_distance_between(self, place_one: Place, place_two: Place) -> float:
        if place_one == place_two:
            return 0.0

        return self.distances_map[place_one, place_two]

    def __hash__(self):
        return 0
