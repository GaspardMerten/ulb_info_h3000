import random
from typing import List

from models import DNA, EnhancedGeneration


def elitist_sample(generation: EnhancedGeneration) -> List[DNA]:
    ordered_generation = list(
        map(lambda t: t[0], sorted(generation, key=lambda x: x[1]))
    )

    generation_size = len(ordered_generation)

    twenty_percent_index = round(generation_size / 5)

    selected_elit_mode = ordered_generation[0:twenty_percent_index]

    random_populace_mode = random.choices(
        ordered_generation[twenty_percent_index:], k=round(generation_size / 5)
    )

    selected_parents_indexes = selected_elit_mode + random_populace_mode

    return selected_parents_indexes


def extreme_elitist_sample(generation: EnhancedGeneration) -> List[DNA]:
    ordered_generation = list(
        map(lambda t: t[0], sorted(generation, key=lambda x: x[1]))
    )

    generation_size = len(ordered_generation)

    two_percent_index = round(generation_size / 50)

    # 8% (2% * 4)
    ultra_elit_mode = ordered_generation[0 : two_percent_index + 1] * 5

    twenty_percent_index = round(generation_size / 5)
    eighty_percent_index = round(generation_size / 10 * 9)

    # Select 10% best
    selected_elit_mode = ordered_generation[0:twenty_percent_index]

    random_populace_mode = random.choices(
        ordered_generation[twenty_percent_index:eighty_percent_index],
        k=round(generation_size / 10),
    )

    return ultra_elit_mode + selected_elit_mode + random_populace_mode
