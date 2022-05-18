import random

from models import DNA


def norse_mutation(dna: DNA) -> DNA:
    dna_list = list(dna)

    if random.random() < 0.5:
        dna_list[20:22] = sorted(random.sample(range(1, 20), 2))

        mutation_places = sorted(random.sample(range(1, 20), 2))
        part = dna_list[mutation_places[0]: mutation_places[1]]
        random.shuffle(part)
        dna_list[mutation_places[0]: mutation_places[1]] = part

        mutation_places = sorted(random.sample(range(1, 20), 2))

        dna_list[mutation_places[0]: mutation_places[1]] = reversed(
            dna_list[mutation_places[0]: mutation_places[1]]
        )
    else:
        mutation_places = sorted(random.sample(range(1, 20), 2))
        dna_fragment = dna_list[mutation_places[0]: mutation_places[1]]
        dna_list[mutation_places[0]: mutation_places[1]] = [-1] * (
                mutation_places[1] - mutation_places[0]
        )
        insert_place = random.randint(1, 20)
        dna_list[insert_place:insert_place] = dna_fragment
        dna_list = [a for a in dna_list if a != -1]

    return tuple(dna_list)
