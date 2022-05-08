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

    def _add_truck_path_from_places(place_1, place_2):
        truck_path = TruckPath(
            place_1,
            place_2,
            global_config.get_distance_between(place_1, place_2),
            place_1.money
        )

        total_path.append(truck_path)

    place1 = global_config.places[0]
    place2 = global_config.places[group_dna[0]]

    _add_truck_path_from_places(place1, place2)

    for i in range(len(group_dna) - 1):
        place1 = global_config.places[group_dna[i]]
        place2 = global_config.places[group_dna[i + 1]]

        _add_truck_path_from_places(place1, place2)

    place1 = global_config.places[group_dna[-1]]
    place2 = global_config.places[0]
    _add_truck_path_from_places(place1, place2)

    return Truck(total_path)


def compute_truck_fitness(truck: Truck) -> float:
    fitness = 0

    for path in truck.paths:
        fitness += path.distance + path.distance * path.money

    return fitness


def divide_by_truck(dna):
    group2_beginning = dna[-2] + 1
    group3_beginning = dna[-1] + 1

    group1 = dna[1:group2_beginning]
    group2 = dna[group2_beginning:group3_beginning]
    group3 = dna[group3_beginning:-2]

    return [group1, group2, group3]
