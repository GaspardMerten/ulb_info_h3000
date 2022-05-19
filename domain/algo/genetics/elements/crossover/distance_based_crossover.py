from __future__ import annotations

import random
from typing import Any, Tuple

from domain.dna import extract_fragments_from_dna
from models import DNA, GlobalConfig

MARK = "LATTER"


def get_latter_city(dna, k):
    position = dna.index(k)

    if len(dna) - 1 == position:
        return dna[0]
    else:

        return dna[position + 1]


def get_former_city(dna: DNA, k):
    if k == 1:
        return dna[-1]
    else:
        return dna[k - 1]


def decode(dna: DNA):
    groups = extract_fragments_from_dna(dna)
    decoded_dna = []

    for group in groups:
        decoded_dna = decoded_dna + [0] + list(group)

    return decoded_dna


def rationalize(dna: DNA) -> tuple[int | Any, ...]:
    dna_list = list(dna)
    a = []

    x = 0

    # Sending all first numbers before first zero to the end
    for v in dna_list:
        if v == 0:
            break
        else:
            x += 1
            a.append(v)
    dna_list = dna_list[x:] + a

    # Deleting consecutive zeros
    zero_index = None
    for i in range(0, len(dna_list) - 1):
        if dna_list[i] == 0 and dna_list[i + 1] == 0:
            zero_index = i
            break

    if zero_index:
        random_index = list(range(2, len(dna_list)))
        dna_list.pop(zero_index)

        del random_index[zero_index : zero_index + 2]

        final_index = random.choice(random_index)
        dna_list.insert(final_index, 0)

    positions = []
    for index, value in enumerate(dna_list):
        if index != 0 and value == 0:
            positions.append(index - 1 - len(positions))

    for i in range(3):
        dna_list.remove(0)
    dna_list.insert(0, 0)

    dna_list = dna_list + positions

    return tuple(dna_list)


def generate_child1(parent_one, parent_two, config: GlobalConfig):
    parent1_part1 = list(parent_one[1:20])
    parent2_part1 = list(parent_two[1:20])

    # Generation of child1
    child1_0 = [0]
    child1_body = hga_algo(parent1_part1, parent2_part1, config)
    # Randomly choosing a group delimited from one of the parents
    if random.randint(0, 1) == 0:
        child1_tail = list(parent_one[20:22])
    else:
        child1_tail = list(parent_two[20:22])

    child1 = tuple(child1_0 + child1_body + child1_tail)

    return child1


def generate_child2(parent_one, parent_two, config: GlobalConfig):
    # Generation of child2
    parent1_decoded = decode(parent_one)
    parent2_decoded = decode(parent_two)

    child2_unrationalized = hga_algo(parent1_decoded, parent2_decoded, config)
    child2 = rationalize(child2_unrationalized)
    return child2


def distance_based_crossover(
    parent_one: DNA, parent_two: DNA, config: GlobalConfig
) -> Tuple[DNA]:
    if random.random() < 0.3:
        return parent_one, parent_two

    child1 = generate_child1(parent_one, parent_two, config)
    child2 = generate_child2(parent_one, parent_two, config)

    return child1, child2


def hga_algo(parent_one, parent_two, config: GlobalConfig):
    parent_one_list = list(parent_one)
    parent_two_list = list(parent_two)

    parent_one_length = len(parent_one_list)
    k = random.choice(list(set(parent_one)))

    result = [k]

    while parent_one_length > 1:
        if MARK == "LATTER":
            x = get_latter_city(parent_one_list, k)
            y = get_latter_city(parent_two_list, k)
        else:
            x = get_former_city(parent_one_list, k)
            y = get_former_city(parent_two_list, k)

        parent_one_list.remove(k)
        parent_two_list.remove(k)

        distance_x_k = config.get_distance_between(config.places[k], config.places[x])
        distance_y_k = config.get_distance_between(config.places[k], config.places[y])

        if distance_x_k < distance_y_k:
            k = x
        else:
            k = y

        result.append(k)
        parent_one_length = len(parent_one_list)

    return result
