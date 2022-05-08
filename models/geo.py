from dataclasses import dataclass

__all__ = ('Place',)


@dataclass(slots=True)
class Place:
    name: str
    lat: float
    long: float
    money: float

    def __hash__(self):
        return self.name.__hash__()
