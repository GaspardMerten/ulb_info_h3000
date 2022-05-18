import random
from typing import Tuple

from domain.algo.genetics.elements.crossover._fix_dna import _fix_dna
from models import DNA


def uniform_crossover(parent_one: DNA, parent_two: DNA, **kwargs) -> Tuple[DNA]:
    parent_one_list = list(parent_one)
    parent_two_list = list(parent_two)

    for index in range(1, 20):
        if random.random() < 0.5:
            parent_one_list[index] = parent_two_list[index]
        else:
            parent_two_list[index] = parent_one_list[index]

    return _fix_dna(parent_one_list), _fix_dna(parent_two_list)
