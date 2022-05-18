from typing import Tuple, Dict

from models.dna import DNA
from models.geo import Place

EnhancedGenerationResult = Dict[DNA, Tuple[float, Tuple[float, float]]]
DistancesMap = Dict[Tuple[Place, Place], float]
