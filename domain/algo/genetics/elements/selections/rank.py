import random
from typing import List

from models import EnhancedGenerationResult, DNA


def rank_sample(generation: EnhancedGenerationResult) -> List[DNA]:
    sorted_generation = sorted(generation.items(), key=lambda x: -x[1][0])

    return random.choices(
        sorted_generation,
        k=round(len(generation) / 2),
        weights=[i + 1 for i in range(len(sorted_generation))],
    )
