from typing import List

from matplotlib import pyplot as plt

from models import Place
from models.truck import Truck


def plot_places_and_show(places: List[Place]):
    _plot_places(places)

    plt.show()


def _plot_places(places):
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


def plot_truck_paths_and_show(trucks: List[Truck], title: str = "") -> object:
    _plot_truck_paths(trucks)

    plt.title(title)

    plt.show()


def _plot_truck_paths(trucks):
    for count, truck in enumerate(trucks):

        compute_max_money = max(*map(lambda p: p.money, truck.paths), 1)

        for path in truck.paths:
            x = []
            y = []

            x.append(path.origin.long)
            x.append(path.destination.long)
            y.append(path.origin.lat)
            y.append(path.destination.lat)

            line_width = max(1, (path.money / compute_max_money) * 4)
            color = ["red", "green", "blue", "cyan"][count % 3]
            plt.plot(x, y, color=color, linewidth=line_width)


def plot_truck_paths_and_places(trucks: List[Truck], places: List[Place], title=''):
    _plot_places(places)
    _plot_truck_paths(trucks)

    plt.title(title)
    plt.show()
