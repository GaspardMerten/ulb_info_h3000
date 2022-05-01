from dataclasses import dataclass
from utils.geo import Place


@dataclass
class TruckPath:
    origin: Place
    money: float
    destination: Place
    distance: int
