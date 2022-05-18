import random
from typing import List

from models import EnhancedGenerationResult, DNA, EnhancedGeneration


def stochastic_universal_sampling(generation: EnhancedGeneration) -> List[DNA]:
    random_populace_mode = random.choices(
        list(map(lambda x: x[0], generation)), k=round(len(generation) / 2), weights=[1 / x[1] for x in generation]
    )

    return random_populace_mode


def elitist_stochastic_universal_sampling(generation: EnhancedGeneration) -> List[DNA]:
    random_populace_mode = random.choices(
        list(map(lambda x: x[0], generation)), k=round(len(generation) / 2), weights=[(1 / x[1]) ** 2 for x in generation]
    )

    return random_populace_mode
