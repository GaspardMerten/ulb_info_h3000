import random
from abc import abstractmethod, ABC
from typing import List, Tuple

from models import EnhancedGenerationResult, EnhancedGeneration
from models.config import GlobalConfig
from models.dna import DNA

__all__ = ("INaturalSelection",)


class INaturalSelection(ABC):
    def __init__(self, config: GlobalConfig):
        self.config: GlobalConfig = config

    def generate_new_generation(
        self,
        old_generation: EnhancedGeneration,
    ) -> List[DNA]:
        old_generation_size = len(old_generation)

        parents = self.select_parents(old_generation)

        assert len(parents) * 2 <= old_generation_size, "Too many parents selected"

        while len(parents) * 2 < old_generation_size:
            parents.append(random.choice(parents))
        new_generation: List[DNA] = []

        for parent_one in parents:
            parent_two = random.choice(list(a for a in parents if a != parent_one))

            new_generation += self.generate_children_from_parents(
                parent_one, parent_two, config=self.config
            )

        return new_generation

    def apply_mutation_to_generation(self, generation: List[DNA]):
        for index, dna in enumerate(generation):
            if random.random() < self.get_mutation_rate(generation):
                generation[index] = self.apply_mutation(dna)

    @abstractmethod
    def get_mutation_rate(self, current_population: List[DNA]) -> float:
        raise NotImplementedError()

    @abstractmethod
    def apply_mutation(self, dna: DNA) -> DNA:
        raise NotImplementedError()

    @abstractmethod
    def generate_children_from_parents(
        self, parent_one: DNA, parent_two: DNA, **kwargs
    ) -> List[DNA]:
        raise NotImplementedError()

    @abstractmethod
    def select_parents(self, generation: EnhancedGenerationResult) -> List[DNA]:
        raise NotImplementedError()

    @abstractmethod
    def get_boosted_dna(self, dna: DNA) -> Tuple[DNA, float]:
        raise NotImplementedError()
