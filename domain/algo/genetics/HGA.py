import random
from typing import List, Dict
from domain.algo.genetics import INaturalSelection
from models import DNA


def get_latter_city(dna: DNA, k):
    if len(dna) == k:
        return dna[1]
    else:
        print(dna)
        print(k)
        return dna[k + 1]


def get_former_city(dna: DNA, k):
    if k == 1:
        return dna[-1]
    else:
        return dna[k - 1]


class HGA(INaturalSelection):
    MARK = "LATTER"  # Can be definied as LATTER or FORMER

    def select_parents(
            self, generation: List[DNA], fitness: Dict[int, int]
    ) -> List[int]:
        ordered_fitness: List[int] = list(
            dict(sorted(fitness.items(), key=lambda item: item[1])).keys()
        )

        twenty_percent_index = round(len(ordered_fitness) / 5)
        selected_elit_mode = ordered_fitness[0:twenty_percent_index]

        random_populace_mode = random.choices(
            ordered_fitness[twenty_percent_index:], k=round(len(ordered_fitness) / 5)
        )

        selected_parents_indexes = selected_elit_mode + random_populace_mode

        return selected_parents_indexes

    def generate_children_from_parents(
            self, parent_one: DNA, parent_two: DNA
    ) -> List[DNA]:
        pass

    def hga_algo(self, parent_one: DNA, parent_two: DNA):
        parent_one_length = len(parent_one)
        k = random.randint(1, parent_one_length)

        result = [k]

        while parent_one_length > 1:
            if self.MARK == "LATTER":
                x = get_latter_city(parent_one, k)
                y = get_latter_city(parent_two, k)
            else:
                x = get_former_city(parent_one, k)
                y = get_former_city(parent_two, k)

            parent_one.remove(k)
            parent_two.remove(k)

            distance_x_k = self.config.get_distance_between(
                self.config.places[k], self.config.places[x]
            )
            distance_y_k = self.config.get_distance_between(
                self.config.places[k], self.config.places[y]
            )

            if distance_x_k < distance_y_k:
                k = x
            else:
                k = y

            result.append(k)
            parent_one_length = len(parent_one)

        return result

    def get_mutation_rate(self, current_population: List[DNA]) -> float:
        return .6

    def apply_mutation(self, dna: DNA) -> DNA:
        random_result = random.random()

        if random_result < 0.5:  # 50%
            return self.apply_type_one_mutation(dna)
        else:
            return self.apply_type_two_mutation(dna)

    def apply_type_one_mutation(self, dna: DNA) -> DNA:
        dna_list = list(dna)

        # Part 1
        mutation_places = sorted(random.sample(range(1, 20), 2))

        dna_list[mutation_places[0]: mutation_places[1]] = reversed(
            dna_list[mutation_places[0]: mutation_places[1]]
        )

        # Part 2
        self.randomize_group_part(dna_list)

        return tuple(dna_list)

    def apply_type_two_mutation(self, dna: DNA) -> DNA:
        dna_list = list(dna)

        # Part 1
        switch_places = sorted(random.sample(range(1, 20), 2))

        group_1, group_2, group_3 = (
            dna_list[1: switch_places[0]],
            dna_list[switch_places[0], switch_places[1]],
            dna_list[switch_places[1], 20],
        )

        dna_list = group_2 + group_1 + group_3 + dna_list[20:22]

        # Part 2
        self.randomize_group_part(dna_list)

        return tuple(dna_list)

    @staticmethod
    def randomize_group_part(dna_list):
        dna_list[20:22] = sorted(random.sample(range(1, 20), 2))
