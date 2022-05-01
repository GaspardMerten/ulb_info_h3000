from typing import List

from matplotlib import pyplot as plt

from models.truck import Truck
from utils.geo import Place


def plot_places_and_show(places: List[Place]):
    x = []
    y = []

    for count, item in enumerate(places):
        x.append(item.long)
        y.append(item.lat)
        plt.annotate(item.name, (x[count], y[count]))

    plt.scatter(
        x,
        y,
    )

    plt.show()


def plot_truck_paths(trucks: List[Truck]):
    for count, truck in enumerate(trucks):
        x = []
        y = []

        for path in truck.paths:
            x.append(path.origin.long)
            x.append(path.destination.long)
            y.append(path.origin.lat)
            y.append(path.destination.lat)

        plt.plot(x, y, color='red')

    plt.show()
