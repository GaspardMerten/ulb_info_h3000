import random
from typing import List

from models import EnhancedGenerationResult, DNA


def stochastic_universal_sampling(generation: EnhancedGenerationResult) -> List[DNA]:
    random_populace_mode = random.choices(
        generation.keys(), k=round(len(generation) / 2), weights=[1 / x[0] for x in generation.values()]
    )

    return random_populace_mode


def elitist_stochastic_universal_sampling(generation: EnhancedGenerationResult) -> List[DNA]:
    random_populace_mode = random.choices(
        generation.keys(), k=round(len(generation) / 2), weights=[(1 / x[0]) ** 2 for x in generation.values()]
    )

    return random_populace_mode
