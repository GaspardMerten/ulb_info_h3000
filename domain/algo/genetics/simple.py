import random
from functools import cache
from math import ceil
from typing import List, Dict

from domain.algo.genetics import INaturalSelection
from domain.compute_fitness import compute_total_fitness
from models import DNA


class SimpleAlgo(INaturalSelection):
    def select_parents(
        self, generation: List[DNA], fitness: Dict[int, float]
    ) -> List[int]:
        ordered_fitness: List[int] = list(
            dict(sorted(fitness.items(), key=lambda item: item[1])).keys()
        )
        ordered_fitness_length = len(ordered_fitness)

        # Select 2% best
        two_percent_index = ceil(ordered_fitness_length / 50)

        ultra_elit_mode = ordered_fitness[0 : two_percent_index + 1] * 4

        twenty_percent_index = round(ordered_fitness_length / 5)
        eighty_percent_index = round(ordered_fitness_length / 10 * 8)

        # Select 20% best
        selected_elit_mode = ordered_fitness[0:twenty_percent_index]

        random_populace_mode = random.choices(
            ordered_fitness[twenty_percent_index:eighty_percent_index],
            k=round(ordered_fitness_length / 4),
        )

        selected_parents_indexes = (
            ultra_elit_mode + selected_elit_mode + random_populace_mode
        )
        return selected_parents_indexes

    def get_mutation_rate(self) -> float:
        return 0.3

    # noinspection PyTypeChecker
    def apply_mutation(self, dna: DNA) -> DNA:
        dna_list = list(dna)

        mutation_type = random.random()
        if mutation_type < 0.2:
            dna_list[20:21] = sorted(random.sample(range(1, 20), 2))

        else:
            mutation_places = sorted(random.sample(range(1, 20), 2))

            dna_list[mutation_places[0] : mutation_places[1]] = reversed(
                dna_list[mutation_places[0] : mutation_places[1]]
            )

        return tuple(dna_list)

    def generate_children_from_parents(
        self, parent_one: DNA, parent_two: DNA
    ) -> List[DNA]:
        switch_places = random.sample(range(1, 20), 3)

        parent_one_list = list(parent_one)
        parent_two_list = list(parent_two)

        for switch_place in switch_places:
            buffer = parent_one_list[switch_place]
            parent_one_list[switch_place] = parent_two_list[switch_place]
            parent_one_list[
                parent_one_list.index(parent_two_list[switch_place])
            ] = buffer

        switch_places = random.sample(range(1, 20), 3)

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

        return [parent_one, parent_two]

    @cache
    def get_boosted_dna(self, dna: DNA) -> DNA:
        dna_list = list(dna)

        dna_without_group = dna_list[0:20]

        max_dna = dna
        max_dna_score = compute_total_fitness(dna, self.config)
        old_dna_score = max_dna_score
        for i in range(4, 12):
            for j in range(i, 16):
                tmp_dna = dna_without_group + [i, j]
                dna_score = compute_total_fitness(tuple(tmp_dna), self.config)

                if dna_score < max_dna_score:
                    max_dna_score = dna_score
                    max_dna = tmp_dna
        print(
            f"\nBoosted DNA: \nFrom {old_dna_score} to {max_dna_score}\nImprovement: {round((1 - max_dna_score / old_dna_score) * 100, 2)}%"
        )
        return tuple(max_dna)
