from functools import cache
from typing import Tuple

from domain.dna import extract_fragments_from_dna, dna_fragment_to_truck
from models import GlobalConfig, Truck, DNA

_AVG_TOTAL_FITNESS_RISK = 8000000000
_AVG_TOTAL_FITNESS_DISTANCE = 70000


@cache
def compute_total_fitness(dna: DNA, global_config: GlobalConfig) -> float:
    """
    Takes a DNA and a global configuration, and returns the total fitness of the DNA

    :param dna: The DNA of the model
    :param global_config: the configuration file contating the list of the places
    :return: The total fitness of the DNA.
    """
    result = compute_total_fitness_separated(dna, global_config)
    return result[0] / _AVG_TOTAL_FITNESS_DISTANCE + result[1] / _AVG_TOTAL_FITNESS_RISK


@cache
def compute_total_fitness_separated(
    dna: DNA, global_config: GlobalConfig
) -> Tuple[float, float]:
    """
    Takes a DNA and a global configuration, and returns the total fitness of the DNA

    :param dna: The DNA of the model
    :param global_config: the configuration file contating the list of the places
    :return: The total fitness of the DNA.
    """
    total_fitness_distance = 0
    total_fitness_risk = 0

    groups = extract_fragments_from_dna(dna)

    for group_dna in groups:
        truck = dna_fragment_to_truck(group_dna, global_config)
        x = compute_truck_fitness(truck)
        fitness_distance, fitness_risk = x
        total_fitness_risk += fitness_risk
        total_fitness_distance += fitness_distance
    return total_fitness_distance, total_fitness_risk


@cache
def compute_truck_fitness(truck: Truck):
    """
    The fitness of a truck is the sum of the distances of all its paths, plus the sum of the distances of all its paths
    multiplied by the money of all its paths

    :param truck: the truck for which to compute the fitness
    :return: The fitness of the truck.
    """
    fitness_distance = 0
    fitness_danger = 0

    current_money = 0

    for path in truck.paths:
        current_money += path.money
        fitness_distance += path.distance  # + path.distance * path.money
        fitness_danger += path.distance * current_money  # + path.distance * path.money

    return [fitness_distance, fitness_danger]
