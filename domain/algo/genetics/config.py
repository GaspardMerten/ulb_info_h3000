from dataclasses import dataclass

__all__ = ("GeneticAlgorithmConfig",)

from typing import Callable

from domain.algo.genetics.interface import INaturalSelection


@dataclass(slots=True)
class GeneticAlgorithmConfig:
    number_of_elements_per_generation: int
    number_of_generations: int
    algo_type: Callable[..., INaturalSelection]
