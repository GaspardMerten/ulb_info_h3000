from dataclasses import dataclass
from typing import List

from models.truck_path import TruckPath


@dataclass(slots=True)
class Truck:
    paths: List[TruckPath]