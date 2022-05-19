import random
from typing import Tuple

from domain.algo.genetics.elements.crossover._fix_dna import _fix_dna
from models import DNA


def multi_point_crossover(parent_one: DNA, parent_two: DNA, **kwargs) -> Tuple[DNA]:
    parent_one_list = list(parent_one)
    parent_two_list = list(parent_two)

    pivots = random.sample(range(1, 21), k=2)

    parent_one_list[pivots[0] : pivots[1]] = parent_two[pivots[0] : pivots[1]]

    parent_two_list[pivots[1] : 20] = parent_one[pivots[1] : 20]
    parent_two_list[1 : pivots[0]] = parent_one[1 : pivots[0]]

    return _fix_dna(parent_one_list), _fix_dna(parent_two_list)
