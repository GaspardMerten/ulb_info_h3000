import abc
import random
from typing import List

from models.dna import DNA

__all__ = ('INaturalSelection',)


class INaturalSelection(abc.ABCMeta):
    @abc.abstractmethod
    def get_mutation_rate(self) -> float:
        pass

    @abc.abstractmethod
    def apply_mutation(self, dna: DNA) -> None:
        pass

    def apply_mutation_to_generation(cls, generation: List[DNA]):
        for dna in generation:
            if random.random() < cls.get_mutation_rate():
                cls.apply_mutation(dna)

    @abc.abstractmethod
    def generate_child_from_parents(self, parent_one: DNA, parent_two: DNA) -> DNA:
        pass

    def generate_new_generation(cls, old_generation: List[DNA]) -> List[DNA]:
        raise NotImplementedError()
