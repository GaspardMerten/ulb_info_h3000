import random

from models import DNA


# noinspection PyTypeChecker
def _generate_random_dna() -> DNA:
    paths: DNA = random.sample(range(1, 20), 19)
    groups: DNA = random.sample(range(1, 20), 2)

    return [0, *paths, *sorted(groups)]
