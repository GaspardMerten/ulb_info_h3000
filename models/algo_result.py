from dataclasses import dataclass, asdict
from typing import List, Type, Any, Dict

from dacite import from_dict

from domain.algo.genetics.config import GeneticAlgorithmConfig
from models import DNA
from models.typedef import EnhancedGenerationResult


@dataclass(slots=True)
class TurnResult:
    dna: DNA
    boost_improvement: float
    generation: int
    fitness: float
    distance_fitness: float
    risk_fitness: float


@dataclass(slots=True)
class AlgoResult:
    config: GeneticAlgorithmConfig
    results: List[TurnResult]
    final_generation: EnhancedGenerationResult
    final_generation: EnhancedGenerationResult

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return from_dict(cls, data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)