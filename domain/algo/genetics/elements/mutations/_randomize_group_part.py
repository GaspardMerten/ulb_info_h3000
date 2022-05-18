import random


def randomize_group_part(dna_list):
    dna_list[20:22] = sorted(random.sample(range(1, 20), 2))