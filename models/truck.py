from dataclasses import dataclass
from truck_path import TruckPath
from typing import List


@dataclass
class Truck:
    paths: List[TruckPath]