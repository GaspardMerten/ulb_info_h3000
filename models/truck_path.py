from dataclasses import dataclass
from models.geo import Place


@dataclass(slots=True, unsafe_hash=True)
class TruckPath:
    origin: Place
    destination: Place
    distance: float
    money: float
