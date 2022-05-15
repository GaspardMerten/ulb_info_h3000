import random
from typing import List, Dict, Tuple, Any
from domain.algo.genetics import INaturalSelection
from domain.compute_fitness import compute_total_fitness
from domain.dna import extract_fragments_from_dna
from models import DNA


def get_latter_city(dna, k):
    print(k)
    print("len" + str(len(dna)))
    print(dna)

    position = dna.index(k)

    if len(dna) - 1 == position:
        return dna[0]
    else:

        return dna[position + 1]


def get_former_city(dna: DNA, k):
    if k == 1:
        return dna[-1]
    else:
        return dna[k - 1]


# noinspection PyTypeChecker
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

    def decode(self, dna: DNA):
        groups = extract_fragments_from_dna(dna)
        decoded_dna = []

        for group in groups:
            decoded_dna = decoded_dna + [0] + list(group)

        return decoded_dna

    def rationalize(self, dna: DNA) -> tuple[int | Any, ...]:
        dna_list = list(dna)
        a = []

        x = 0

        # Sending all first numbers before first zero to the end
        for v in dna_list:
            if v == 0:
                break
            else:
                x += 1
                a.append(v)
        dna_list = dna_list[x:] + a

        # Deleting consecutive zeros
        zero_index = None
        for i in range(0, len(dna_list) - 1):
            if dna_list[i] == 0 and dna_list[i+1] == 0:
                zero_index = i
                break

        if zero_index:
            random_index = list(range(2, len(dna_list)))
            dna_list.pop(zero_index)

            del random_index[zero_index:zero_index+2]

            final_index = random.choice(random_index)
            dna_list.insert(final_index, 0)

        positions = []
        for index, value in enumerate(dna_list):
            if index != 0 and value == 0:
                positions.append(index - 1 - len(positions))
        print("dsds" + str(dna_list))

        for i in range(3):
            dna_list.remove(0)
        dna_list.insert(0, 0)


        dna_list = dna_list + positions

        return tuple(dna_list)

    def generate_child1(self, parent_one, parent_two):
        parent1_part1 = list(parent_one[1:20])
        parent2_part1 = list(parent_two[1:20])

        # Generation of child1
        child1_0 = [0]
        child1_body = self.hga_algo(parent1_part1, parent2_part1)
        # Randomly choosing a group delimited from one of the parents
        if random.randint(0, 1) == 0:
            child1_tail = list(parent_one[20:22])
        else:
            child1_tail = list(parent_two[20:22])

        child1 = tuple(child1_0 + child1_body + child1_tail)

        return child1

    def generate_child2(self, parent_one, parent_two):
        # Generation of child2
        parent1_decoded = self.decode(parent_one)
        parent2_decoded = self.decode(parent_two)

        child2_unrationalized = self.hga_algo(parent1_decoded, parent2_decoded)
        child2 = self.rationalize(child2_unrationalized)
        return child2

    def generate_children_from_parents(
            self, parent_one: DNA, parent_two: DNA
    ) -> List[DNA]:

        child1 = self.generate_child1(parent_one, parent_two)
        child2 = self.generate_child2(parent_one, parent_two)

        return child1, child2

    def hga_algo(self, parent_one, parent_two):
        parent_one_list = list(parent_one)
        parent_two_list = list(parent_two)
        parent_one_length = len(parent_one_list)
        k = random.choice(list(set(parent_one)))

        print("PARENR1" + str(len(parent_one_list)))

        result = [k]

        while parent_one_length > 1:
            if self.MARK == "LATTER":
                print("parent1")
                x = get_latter_city(parent_one_list, k)
                print("parent2")
                y = get_latter_city(parent_two_list, k)
            else:
                x = get_former_city(parent_one_list, k)
                y = get_former_city(parent_two_list, k)

            parent_one_list.remove(k)
            parent_two_list.remove(k)

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
            parent_one_length = len(parent_one_list)
            print("result = " + str(result))

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
