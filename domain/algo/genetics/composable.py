from typing import List, Dict, Callable

from domain.algo.genetics.HGAXSIMPLE import HGAXSimple
from models import DNA, EnhancedGenerationResult, GlobalConfig, EnhancedGeneration


class Composable(HGAXSimple):
    def __init__(self, select_parents: Callable[[EnhancedGeneration], List[DNA]],
                 generate_children_from_parents: Callable[[EnhancedGeneration], List[DNA]],
                 apply_mutation: Callable[[DNA], DNA], config: GlobalConfig):
        self.select_parents = select_parents
        self.generate_children_from_parents = generate_children_from_parents
        self.apply_mutation = apply_mutation
        super().__init__(config)
