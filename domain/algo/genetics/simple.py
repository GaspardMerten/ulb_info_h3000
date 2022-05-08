import random
from typing import List, Dict
from domain.algo.genetics import INaturalSelection
from models import DNA


class SimpleAlgo(INaturalSelection):
    def select_parents(self, generation: List[DNA], fitness: Dict[int, float]) -> List[int]:
        ordered_fitness: List[int] = list(dict(sorted(fitness.items(), key=lambda item: item[1])).keys())
        # Select 20% best
        twenty_percent_index = round(len(ordered_fitness) / 5)
        selected_elit_mode = ordered_fitness[0:twenty_percent_index]

        random_populace_mode = random.choices(ordered_fitness[twenty_percent_index:],
                                              k=round(len(ordered_fitness) / 10))

        selected_parents_indexes = selected_elit_mode + random_populace_mode

        return selected_parents_indexes

    def get_mutation_rate(self) -> float:
        return 0.2

    def apply_mutation(self, dna: DNA) -> None:
        mutation_places = random.sample(range(1, 20), 2)

        buffer = dna[mutation_places[0]]

        dna[mutation_places[0]] = dna[mutation_places[1]]
        dna[mutation_places[1]] = buffer

    def generate_children_from_parents(self, parent_one: DNA, parent_two: DNA) -> List[DNA]:
        switch_places = random.sample(range(1, 20), 10)

        for switch_place in switch_places:
            buffer = parent_one[switch_place]
            parent_one[switch_place] = parent_two[switch_place]
            parent_one[parent_one.index(parent_two[switch_place])] = buffer

        if 0.5 < random.random():
            parent_one = parent_one[0:20] + parent_two[20:22]

        return [parent_one, parent_two]
