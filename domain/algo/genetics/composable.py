from typing import List, Dict, Callable

from domain.algo.genetics.HGAXSIMPLE import HGAXSimple
from models import DNA, EnhancedGenerationResult, GlobalConfig


class Composable(HGAXSimple):
    def __init__(self, select_parents: Callable[[EnhancedGenerationResult], List[DNA]], config: GlobalConfig):
        self.select_parents = select_parents

        super().__init__(config)
