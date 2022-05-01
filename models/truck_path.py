from dataclasses import dataclass
from utils.geo import Place


@dataclass
class TruckPath:
    origin: Place
    money: fl
    destination: Place
    distance: int
