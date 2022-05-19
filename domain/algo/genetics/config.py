from dataclasses import dataclass

__all__ = ("GeneticAlgorithmConfig",)

from typing import Callable, List

from models import DNA, EnhancedGeneration


@dataclass(slots=True)
class GeneticAlgorithmConfig:
    number_of_elements_per_generation: int
    number_of_generations: int
    selection: Callable[[EnhancedGeneration], List[DNA]]
    crossover: Callable[[EnhancedGeneration], List[DNA]]
    mutation: Callable[[DNA], DNA]
