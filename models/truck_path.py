from dataclasses import dataclass
from models.geo import Place


@dataclass(slots=True)
class TruckPath:
    origin: Place
    destination: Place
    money: float
    distance: int
    money: float
