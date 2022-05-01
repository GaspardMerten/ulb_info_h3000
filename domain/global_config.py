from dataclasses import dataclass
from typing import List
from utils.geo import Place

@dataclass
class GlobalConfig:
    places: List[Place]

    def add_place(self, place: Place):
        self.places.append(place)
