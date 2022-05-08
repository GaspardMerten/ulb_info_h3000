from dataclasses import dataclass

__all__ = ('GeneticAlgorithmConfig',)


@dataclass(slots=True)
class GeneticAlgorithmConfig:
    number_of_elements: int
    number_of_generations: int
