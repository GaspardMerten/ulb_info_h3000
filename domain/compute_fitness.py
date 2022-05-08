from models.truck import Truck
from models.truck_path import TruckPath
from domain.global_config import GlobalConfig
from models.geo import get_distance_between


def compute_total_fitness(dna):
    pass


def index_to_trucks(dna, global_config: GlobalConfig):
    trucks = []
    for truck_points in dna:
        total_path = []
        for i in range(len(truck_points) - 1):
            place1 = global_config.places[i]
            place2 = global_config.places[i+1]
            truck_path = TruckPath(
                place1,
                place2,
                get_distance_between(place1, place2),
                place1.money
            )

def compute_truck_fitness(truck: Truck) -> float:
    fitness = 0
    for path in truck.paths:
        fitness += (path.distance + path.distance * path.money)

    return fitness


def divide_by_truck(dna):
    group2_beginning = dna[-2] + 1
    group3_beginning = dna[-1] + 1

    group1 = dna[1:group2_beginning]
    group2 = dna[group2_beginning:group3_beginning]
    group3 = dna[group3_beginning:-2]

    return group1, group2, group3
