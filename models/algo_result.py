from dataclasses import dataclass
from typing import List, Type, Dict, Tuple

from domain.algo.genetics.config import GeneticAlgorithmConfig
from models import DNA


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
    final_generation: Dict[DNA, Tuple[float, Tuple[float, float]]]
