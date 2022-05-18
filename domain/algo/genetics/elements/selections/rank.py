import random
from typing import List

from models import DNA, EnhancedGeneration


def rank_sample(generation: EnhancedGeneration) -> List[DNA]:
    sorted_generation = list(map(lambda x : x[0], sorted(generation, key=lambda x: -x[1])))

    return random.choices(
        sorted_generation,
        k=round(len(generation) / 2),
        weights=[i + 1 for i in range(len(sorted_generation))],
    )
