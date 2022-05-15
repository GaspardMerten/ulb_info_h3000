import random
from functools import cache
from math import ceil
from typing import List, Dict, Tuple

from domain.algo.genetics.HGA import HGA
from domain.algo.genetics.interface import INaturalSelection
from domain.compute_fitness import compute_total_fitness
from models import DNA


class HGAXSimple(HGA):
    def select_parents(
            self, generation: List[DNA], fitness: Dict[int, float]
    ) -> List[int]:
        ordered_fitness: List[int] = list(
            dict(sorted(fitness.items(), key=lambda item: item[1])).keys()
        )
        ordered_fitness_length = len(ordered_fitness)

        two_percent_index = ceil(ordered_fitness_length / 50)

        # 8% (2% * 4)
        ultra_elit_mode = ordered_fitness[0: two_percent_index + 1] * 5

        twenty_percent_index = round(ordered_fitness_length / 5)
        eighty_percent_index = round(ordered_fitness_length / 10 * 9)

        # Select 10% best
        selected_elit_mode = ordered_fitness[0:twenty_percent_index]

        random_populace_mode = random.choices(
            ordered_fitness[twenty_percent_index:eighty_percent_index],
            k=round(ordered_fitness_length / 10),
        )

        selected_parents_indexes = (
                ultra_elit_mode + selected_elit_mode + random_populace_mode
        )
        assert (
                len(selected_parents_indexes) < len(generation) / 2
        ), "Too many selected parents"

        return selected_parents_indexes

    def get_mutation_rate(self, current_population: List[DNA]) -> float:
        return .6

    # noinspection PyTypeChecker
    def apply_mutation(self, dna: DNA) -> DNA:
        dna_list = list(dna)

        if random.random() < .5:
            dna_list[20:22] = sorted(random.sample(range(1, 20), 2))

            mutation_places = sorted(random.sample(range(1, 20), 2))
            part = dna_list[mutation_places[0]: mutation_places[1]]
            random.shuffle(part)
            dna_list[mutation_places[0]: mutation_places[1]] = part

            mutation_places = sorted(random.sample(range(1, 20), 2))

            dna_list[mutation_places[0]: mutation_places[1]] = reversed(
                dna_list[mutation_places[0]: mutation_places[1]]
            )
        else:
            mutation_places = sorted(random.sample(range(1, 20), 2))
            dna_fragment = dna_list[mutation_places[0]: mutation_places[1]]
            dna_list[mutation_places[0]: mutation_places[1]] = [-1] * (mutation_places[1] - mutation_places[0])
            insert_place = random.randint(1, 20)
            dna_list[insert_place:insert_place] = dna_fragment
            dna_list = [a for a in dna_list if a != -1]

        return tuple(dna_list)
