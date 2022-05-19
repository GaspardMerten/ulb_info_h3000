import random

from models import EnhancedGeneration, Generation


def tournament_sample(generation: EnhancedGeneration) -> Generation:
    return list(map(lambda x: x[0], _tournament_sample(generation)))


def _tournament_sample(generation: EnhancedGeneration) -> EnhancedGeneration:
    winners = []
    for _ in range(round(len(generation) / 2)):
        duelists = random.choices(generation, k=2)

        if duelists[1][1] > duelists[0][1]:
            winner = duelists[0]
        else:
            winner = duelists[1]

        winners.append(winner)

    return winners


def tournament_sample_k2(generation: EnhancedGeneration) -> Generation:
    winners = tournament_sample(_tournament_sample(generation))

    return winners


def tournament_with_elimination_of_winners_sample(
    generation: EnhancedGeneration,
) -> Generation:
    winners = []
    for _ in range(round(len(generation) / 2)):
        duelists = random.choices(generation, k=2)

        if duelists[1][1] > duelists[0][1]:
            winner = duelists[0]
        else:
            winner = duelists[1]

        generation.remove(winner)
        winners.append(winner[0])

    return winners
