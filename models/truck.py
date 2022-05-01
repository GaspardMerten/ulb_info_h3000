from dataclasses import dataclass
from truck_path import TruckPath

@dataclass
class Truck:
    paths: TruckPath[]
    money: float
