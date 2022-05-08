from domain.geo import get_distance_between
from models import GlobalConfig, TruckPath, Truck


def compute_total_fitness(dna, global_config):
    total_fitness = 0
    groups = divide_by_truck(dna)
    for group_dna in groups:
        truck = index_to_truck(group_dna, global_config)
        total_fitness += compute_truck_fitness(truck)

    return total_fitness


def index_to_truck(group_dna, global_config: GlobalConfig):
    total_path = []

    for i in range(len(group_dna) - 1):
        place1 = global_config.places[i]
        place2 = global_config.places[i + 1]
        truck_path = TruckPath(
            place1,
            place2,
            get_distance_between(place1, place2),
            place1.money
        )

        total_path.append(truck_path)

    return Truck(total_path)


def compute_truck_fitness(truck: Truck) -> float:
    fitness = 0
    for path in truck.paths:
        print(path.distance)
        print(path.money)
        fitness += path.distance + path.distance * path.money

    return fitness


def divide_by_truck(dna):
    group2_beginning = dna[-2] + 1
    group3_beginning = dna[-1] + 1

    group1 = dna[1:group2_beginning]
    group2 = dna[group2_beginning:group3_beginning]
    group3 = dna[group3_beginning:-2]

    return [group1, group2, group3]
