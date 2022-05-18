import random
from typing import Tuple

from domain.algo.genetics.elements.crossover._fix_dna import _fix_dna
from models import DNA


def one_point_crossover(parent_one: DNA, parent_two: DNA, **kwargs) -> Tuple[DNA]:
    parent_one_list = list(parent_one)
    parent_two_list = list(parent_two)

    pivot = random.randint(1, 20)

    parent_one_list[pivot: 20] = parent_two[pivot: 20]
    parent_two_list[1: pivot] = parent_one[1: pivot]

    return _fix_dna(parent_one_list), _fix_dna(parent_two_list)
