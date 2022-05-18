import random
from typing import Tuple

from models import DNA


def shuffle_and_swap_crossover(parent_one: DNA, parent_two: DNA, **kwargs) -> Tuple[DNA, DNA]:
    switch_places = random.sample(range(1, 20), random.randint(1, 10))

    parent_one_list = list(parent_one)
    parent_two_list = list(parent_two)

    for switch_place in switch_places:
        buffer = parent_one_list[switch_place]
        parent_one_list[switch_place] = parent_two_list[switch_place]
        parent_one_list[
            parent_one_list.index(parent_two_list[switch_place])
        ] = buffer

    switch_places = random.sample(range(1, 20), random.randint(1, 10))

    for switch_place in switch_places:
        buffer = parent_two_list[switch_place]
        parent_two_list[switch_place] = parent_one_list[switch_place]
        parent_two_list[
            parent_two_list.index(parent_one_list[switch_place])
        ] = buffer

    parent_two = tuple(parent_two_list)
    parent_one = tuple(parent_one_list)

    if 0.2 < random.random():
        parent_one = parent_one[0:20] + parent_two[20:22]

    if 0.2 < random.random():
        parent_two = parent_two[0:20] + parent_one[20:22]

    return parent_one, parent_two
