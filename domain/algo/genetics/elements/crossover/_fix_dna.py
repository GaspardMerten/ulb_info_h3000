from models import DNA


def _fix_dna(dna: DNA) -> DNA:
    dna_list = list(dna)

    missing_values = list(set(range(1, 20)) - set(dna[1:20]))

    for index, value in enumerate(dna[1:20], start=1):
        if value in dna[index + 1 : 20]:
            dna_list[index] = missing_values[0]
            missing_values.pop(0)

    return tuple(dna_list)
