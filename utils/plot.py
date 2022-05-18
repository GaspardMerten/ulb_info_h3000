import dataclasses
import json
import uuid
from typing import List

from matplotlib import pyplot as plt

from domain.dna import dna_fragment_to_truck, extract_fragments_from_dna
from models import Place, GlobalConfig
from models.algo_result import TurnResult, AlgoResult
from models.truck import Truck
from utils.pareto import extract_pareto_from_generation
from models.typedef import EnhancedGenerationResult


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def plot_algo_result(
        result: AlgoResult, config: GlobalConfig, name_builder: uuid.uuid4
):
    fig, axs = plt.subplots(figsize=(10, 15), nrows=3, ncols=2)

    fig.suptitle("Algo result")

    _plot_bests_scores_on_graph(axs[0][0], turns=result.results)
    _plot_bests_evolution_on_graph(axs[0][1], turns=result.results)
    _plot_generations_on_graph(axs[1][0], generation=result.final_generation)
    _plot_truck_paths(
        axs[1][1],
        trucks=[
            dna_fragment_to_truck(frag, config)
            for frag in extract_fragments_from_dna(result.results[-1].dna)
        ],
    )
    _plot_places(axs[1][1], places=config.places)
    extract_and_plot_pareto_on_graph(axs[2][0], generation=result.final_generation)

    plt.savefig(f"results/{name_builder()}.png")
    plt.show()


def extract_and_plot_pareto_on_graph(ax, generation: EnhancedGenerationResult):
    pareto_generation = extract_pareto_from_generation(generation)

    _plot_generations_on_graph(ax, pareto_generation)


def _plot_bests_scores_on_graph(ax, turns: List[TurnResult]):
    z = []
    a = []
    t = []

    for item in turns:
        z.append(item.distance_fitness)
        a.append(item.risk_fitness)
        t.append((item.generation, (item.distance_fitness, item.risk_fitness)))

    ax.scatter(z, a, s=[1 for _ in range(len(z))])

    for ele in t:
        ax.annotate(ele[0], ele[1])


def _plot_bests_evolution_on_graph(ax, turns: List[TurnResult]):
    x = []
    y = []

    for item in turns:
        x.append(item.generation)
        y.append(item.fitness)
        ax.annotate(round(item.fitness, 2), (item.generation, item.fitness))

    ax.plot(x, y)


def _plot_generations_on_graph(ax, generation: EnhancedGenerationResult):
    z = []
    a = []

    for fitness, values in generation.values():
        z.append(values[0])
        a.append(values[1])

    ax.scatter(z, a)


def plot_places_and_show(places: List[Place]):
    _plot_places(places, plt)

    plt.show()


def _plot_places(ax, places):
    x = []
    y = []
    for count, item in enumerate(places):
        x.append(item.long)
        y.append(item.lat)
        ax.annotate(item.name, (x[count], y[count]))
    ax.scatter(
        x,
        y,
    )


def plot_truck_paths_and_show(trucks: List[Truck], title: str = "") -> object:
    _plot_truck_paths(plt, trucks)

    plt.title(title)

    plt.show()


def _plot_truck_paths(ax, trucks):
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
            ax.plot(x, y, color=color, linewidth=line_width)


def plot_truck_paths_and_places(trucks: List[Truck], places: List[Place], title=""):
    plt.title(title)

    _plot_places(plt, places)
    _plot_truck_paths(plt, trucks)

    plt.title(title)
    plt.show()
