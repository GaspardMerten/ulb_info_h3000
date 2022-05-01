from typing import List

from matplotlib import pyplot as plt

from utils.geo import Place


def plot_places(places: List[Place]):
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
