import random

from domain.algo.genetics.elements.mutations._randomize_group_part import (
    randomize_group_part,
)
from models import DNA


def inversion_mutation(dna: DNA) -> DNA:
    a, b = sorted(random.sample(range(1, 21), k=2))
    dna_list = list(dna)

    dna_list[a:b] = reversed(dna_list[a:b])

    randomize_group_part(dna_list)

    return tuple(dna_list)
