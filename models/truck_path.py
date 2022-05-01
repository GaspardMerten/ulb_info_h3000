from dataclasses import dataclass
from utils.geo import Place


@dataclass
class TruckPath:
    origin: Place
    destination: Place
    distance: int
    money: float
