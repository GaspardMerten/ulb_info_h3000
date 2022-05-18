from dataclasses import dataclass
from typing import List, Type

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
    algo: Type
    config: GeneticAlgorithmConfig
    results: List[TurnResult]
    final_generation: EnhancedGenerationResult
