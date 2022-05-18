import random

from domain.algo.genetics.elements.mutations._randomize_group_part import randomize_group_part
from models import DNA


def swap_mutation(dna: DNA) -> DNA:
    a, b = sorted(random.sample(range(1, 21), k=2))

    dna_list = list(dna)

    buffer = dna_list[a]

    dna_list[a] = dna_list[b]
    dna_list[b] = buffer

    randomize_group_part(dna_list)

    return tuple(dna)
