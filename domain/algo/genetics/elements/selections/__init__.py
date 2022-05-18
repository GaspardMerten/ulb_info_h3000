from domain.algo.genetics.elements.selections.elitist import (
    extreme_elitist_sample,
    elitist_sample,
)
from domain.algo.genetics.elements.selections.rank import rank_sample
from domain.algo.genetics.elements.selections.sus import (
    elitist_stochastic_universal_sampling,
    stochastic_universal_sampling,
)
from domain.algo.genetics.elements.selections.tournament import (
    tournament_sample,
    tournament_with_elimination_of_winners_sample,
    tournament_sample_k2,
)

selections = [
    elitist_sample,
    extreme_elitist_sample,
    rank_sample,
    stochastic_universal_sampling,
    elitist_stochastic_universal_sampling,
    tournament_sample,
    tournament_sample_k2,
    tournament_with_elimination_of_winners_sample,
]
