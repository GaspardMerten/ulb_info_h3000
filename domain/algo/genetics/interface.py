import random
from abc import abstractmethod, ABC
from typing import List, Dict

from models import GlobalConfig
from models.dna import DNA

__all__ = ("INaturalSelection",)


class INaturalSelection(ABC):
    def __init__(self, config: GlobalConfig):
        self.config: GlobalConfig = config

    def generate_new_generation(
        self,
        old_generation: List[DNA],
        fitness: Dict[int, int],
        children_per_mating: int = 2,
    ) -> List[DNA]:
        old_generation_size = len(old_generation)

        parents_index = self.select_parents(old_generation, fitness)

        full_parents_index = [*parents_index]

        while len(full_parents_index) * 2 < old_generation_size:
            full_parents_index.append(random.choice(parents_index))

        new_generation: List[DNA] = []

        for parent_one in full_parents_index:
            parent_two = random.choice(
                list(a for a in parents_index if a != parent_one)
            )
            new_generation += self.generate_children_from_parents(
                old_generation[parent_one], old_generation[parent_two]
            )

        return new_generation

    def apply_mutation_to_generation(self, generation: List[DNA]):
        for index, dna in enumerate(generation):
            if random.random() < self.get_mutation_rate():
                generation[index] = self.apply_mutation(dna)

    @abstractmethod
    def get_mutation_rate(self) -> float:
        raise NotImplemented()

    @abstractmethod
    def apply_mutation(self, dna: DNA) -> None:
        raise NotImplemented()

    @abstractmethod
    def generate_children_from_parents(
        self, parent_one: DNA, parent_two: DNA
    ) -> List[DNA]:
        raise NotImplemented()

    @abstractmethod
    def select_parents(
        self, generation: List[DNA], fitness: Dict[int, int]
    ) -> List[int]:
        raise NotImplementedError()

    @abstractmethod
    def get_boosted_dna(self, dna: DNA) -> DNA:
        raise NotImplementedError()
