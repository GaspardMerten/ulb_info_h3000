from functools import lru_cache
from typing import List, Callable, Tuple

from domain.algo.genetics.interface import INaturalSelection
from domain.compute_fitness import compute_total_fitness
from models import DNA, GlobalConfig, EnhancedGeneration, EnhancedGenerationResult


class Composable(INaturalSelection):
    def __init__(
            self,
            select_parents: Callable[[EnhancedGeneration], List[DNA]],
            generate_children_from_parents: Callable[[EnhancedGeneration], List[DNA]],
            apply_mutation: Callable[[DNA], DNA],
            config: GlobalConfig,
            mutation_rate: float,
    ):
        self.select_parents = select_parents
        self.generate_children_from_parents = generate_children_from_parents
        self.apply_mutation = apply_mutation
        self.mutation_rate = mutation_rate
        super().__init__(config)

    def get_mutation_rate(self, current_population: List[DNA]) -> float:
        return self.mutation_rate

    def select_parents(self, generation: EnhancedGenerationResult) -> List[DNA]:
        return []

    def generate_children_from_parents(
        self, parent_one: DNA, parent_two: DNA, **kwargs
    ) -> List[DNA]:
        return []

    def apply_mutation(self, dna: DNA) -> DNA:
        return []

    @lru_cache(10000)
    def get_boosted_dna(self, dna: DNA) -> Tuple[DNA, float]:
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

        improvement_percentage = round((1 - max_dna_score / old_dna_score) * 100, 2)

        return tuple(max_dna), improvement_percentage
