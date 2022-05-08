from dataclasses import dataclass
from models.geo import Place


@dataclass
class TruckPath:
    origin: Place
    destination: Place
    money: float
    distance: int
    money: float
