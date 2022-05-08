from models import GlobalConfig, TruckPath, Truck
from utils.cache import cache


@cache.memoize()
def compute_total_fitness(dna, global_config) -> float:
    """
    Takes a DNA and a global configuration, and returns the total fitness of the DNA

    :param dna: The DNA of the model
    :param global_config: the configuration file contating the list of the places
    :return: The total fitness of the DNA.
    """
    total_fitness = 0

    groups = divide_by_truck(dna)

    for group_dna in groups:
        truck = index_to_truck(group_dna, global_config)
        total_fitness += compute_truck_fitness(truck)

    return total_fitness


def index_to_truck(group_dna, global_config: GlobalConfig) -> Truck:
    """
    Based on the information in the DNA of the truck, creating a truck object containing the list of path that if
    will go through

    :param group_dna: This is the DNA of the group. It's a list of integers, where each integer represents the index of a
    place in the global_config.places list
    :param global_config: GlobalConfig
    :type global_config: GlobalConfig
    :return: The truck inferred by the DNA group
    """
    total_path = []

    if not group_dna:
        return Truck(total_path)

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
    """
    The fitness of a truck is the sum of the distances of all its paths, plus the sum of the distances of all its paths
    multiplied by the money of all its paths

    :param truck: the truck for which to compute the fitness
    :return: The fitness of the truck.
    """
    fitness = 0

    for path in truck.paths:
        fitness += path.distance + path.distance * path.money

    return fitness


def divide_by_truck(dna):
    """
    Takes a DNA sequence and returns a list of three DNA sequences, each of which is a subsequence of the original.
    It is used in order to divide the whole DNA in a group of 3 DNA's. It must be noted that the first number (0)
    always represents the National Bank and that the last two represent where to cut the groups.

    :param dna: the DNA string
    :return: A list of lists.
    """
    group2_beginning = dna[-2] + 1
    group3_beginning = dna[-1] + 1

    group1 = dna[1:group2_beginning]
    group2 = dna[group2_beginning:group3_beginning]
    group3 = dna[group3_beginning:-2]

    return [group1, group2, group3]
