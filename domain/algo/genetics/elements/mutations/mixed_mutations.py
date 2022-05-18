import random

from domain.algo.genetics.elements.mutations.inversion_mutation import inversion_mutation
from domain.algo.genetics.elements.mutations.scramble_mutation import scramble_mutation
from domain.algo.genetics.elements.mutations.swap_mutation import swap_mutation
from models import DNA


def inversion_or_swap_mutation(dna: DNA) -> DNA:
    if random.random() < 0.5:
        return swap_mutation(dna)
    else:
        return inversion_mutation(dna)


def inversion_or_swap_or_scramble_mutation(dna: DNA) -> DNA:
    random_random = random.random()
    if random_random < 0.3:
        return swap_mutation(dna)
    elif random_random < 0.7:
        return inversion_mutation(dna)
    else:
        return scramble_mutation(dna)
