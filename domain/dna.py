import random

from models import DNA, DNA_PATH


# noinspection PyTypeChecker
def _generate_random_dna() -> DNA:
    paths: DNA_PATH = random.sample(range(1, 20), 19)
    groups: DNA_PATH = random.sample(range(1, 20), 2)

    return [0, *paths, *groups]
