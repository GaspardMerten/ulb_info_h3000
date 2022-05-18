from dataclasses import dataclass

__all__ = ("Place",)


@dataclass(slots=True, unsafe_hash=True)
class Place:
    name: str
    lat: float
    long: float
    money: float


