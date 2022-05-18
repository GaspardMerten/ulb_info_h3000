import random
from typing import List

from models import EnhancedGenerationResult, DNA


def tournament_sample(generation: EnhancedGenerationResult) -> List[DNA]:
    winners = []
    for _ in range(len(generation)):
        duelists = random.choices(generation.keys(), k=2)

        if generation[duelists][0] > generation[duelists][1]:
            winner = generation[duelists][1]
        else:
            winner = generation[duelists][0]

        winners.append(winner)

    return winners


def tournament_sample_k2(generation: EnhancedGenerationResult) -> List[DNA]:
    winners = tournament_sample(tournament_sample(generation))

    return winners


def tournament_with_elimination_of_winners_sample(generation: EnhancedGenerationResult) -> List[DNA]:
    winners = []
    for _ in range(len(generation)):
        duelists = random.choices(generation.keys(), k=2)

        if generation[duelists][0] > generation[duelists][1]:
            winner = generation[duelists][1]
        else:
            winner = generation[duelists][0]

        generation.pop(winner)
        winners.append(winner)

    return winners
