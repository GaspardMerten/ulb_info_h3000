from abc import ABC, abstractmethod, ABCMeta
import random
from typing import List

from models.dna import DNA

__all__ = ('INaturalSelection',)


class INaturalSelection(ABCMeta):
    @abstractmethod
    def get_mutation_rate(self) -> float:
        raise NotImplemented()

    @abstractmethod
    def apply_mutation(self, dna: DNA) -> None:
        raise NotImplemented()

    @abstractmethod
    def apply_mutation_to_generation(cls, generation: List[DNA]):
        for dna in generation:
            if random.random() < cls.get_mutation_rate():
                cls.apply_mutation(dna)

    @abstractmethod
    def generate_child_from_parents(self, parent_one: DNA, parent_two: DNA) -> DNA:
        raise NotImplemented()

    @abstractmethod
    def generate_new_generation(cls, old_generation: List[DNA], fitness: List[int]) -> List[DNA]:
        raise NotImplementedError()
