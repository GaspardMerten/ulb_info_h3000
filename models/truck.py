from dataclasses import dataclass
from typing import Tuple

from models.truck_path import TruckPath


@dataclass(slots=True, unsafe_hash=True)
class Truck:
    paths: Tuple[TruckPath]

    @property
    def money(self):
        return sum(path.money for path in self.paths)
