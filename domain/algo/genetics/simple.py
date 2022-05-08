import random
from typing import List

from domain.algo.genetics import INaturalSelection
from models import DNA


class SimpleAlgo(INaturalSelection):
    def get_mutation_rate(self) -> float:
        return 0.01

    def apply_mutation(self, dna: DNA) -> None:
        mutation_places = random.sample(range(1, 20), 2)

        buffer = dna[mutation_places[0]]

        dna[mutation_places[0]] = dna[mutation_places[1]]
        dna[mutation_places[1]] = buffer

    def generate_child_from_parents(self, parent_one: DNA, parent_two: DNA) -> DNA:
        pass

    def generate_new_generation(cls, old_generation: List[DNA], fitness: List[int]) -> List[DNA]:
        pass
