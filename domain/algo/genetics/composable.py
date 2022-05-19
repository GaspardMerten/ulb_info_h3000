from typing import List, Callable

from domain.algo.genetics.interface import INaturalSelection
from models import DNA, GlobalConfig, EnhancedGeneration


class Composable(INaturalSelection):
    def __init__(
        self,
        select_parents: Callable[[EnhancedGeneration], List[DNA]],
        generate_children_from_parents: Callable[[EnhancedGeneration], List[DNA]],
        apply_mutation: Callable[[DNA], DNA],
        config: GlobalConfig,
    ):
        self.select_parents = select_parents
        self.generate_children_from_parents = generate_children_from_parents
        self.apply_mutation = apply_mutation
        super().__init__(config)

    def get_mutation_rate(self, current_population: List[DNA]) -> float:
        return 0.6
