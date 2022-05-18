from typing import Tuple, Dict, List

from models.dna import DNA
from models.geo import Place

EnhancedGenerationResult = Dict[DNA, Tuple[float, Tuple[float, float]]]
Generation = List[DNA]
EnhancedGeneration = List[Tuple[DNA, float]]
DistancesMap = Dict[Tuple[Place, Place], float]
