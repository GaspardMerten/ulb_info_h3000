import random
from functools import cache
from typing import Tuple

from models import GlobalConfig, TruckPath, Truck, DNA, DNAFragment


@cache
def dna_fragment_to_truck(group_dna: DNAFragment, global_config: GlobalConfig) -> Truck:
    """
    Based on the information in the DNA of the truck, creating a truck object containing the list of path that if
    will go through

    :param group_dna: This is the DNA of the group. It's a list of integers, where each integer represents the index of a
    place in the global_config.places list
    :param global_config: GlobalConfig
    :type global_config: GlobalConfig
    :return: The truck inferred by the DNA group
    """

    # Add start and stop
    group_dna = [0, *group_dna, 0]

    total_path = []

    for i in range(len(group_dna) - 1):
        place_1 = global_config.places[group_dna[i]]
        place_2 = global_config.places[group_dna[i + 1]]

        total_path.append(
            TruckPath(
                place_1,
                place_2,
                global_config.get_distance_between(place_1, place_2),
                place_1.money,
            )
        )

    return Truck(tuple(total_path))


@cache
def extract_fragments_from_dna(
    dna: DNA,
) -> Tuple[DNAFragment, DNAFragment, DNAFragment]:
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

    return group1, group2, group3


# noinspection PyTypeChecker
def generate_random_dna() -> DNA:
    paths: DNA = random.sample(range(1, 20), 19)
    groups: DNA = random.sample(range(1, 20), 2)

    return 0, *paths, *sorted(groups)
