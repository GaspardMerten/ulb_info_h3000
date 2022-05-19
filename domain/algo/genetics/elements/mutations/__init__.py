from domain.algo.genetics.elements.mutations.inversion_mutation import (
    inversion_mutation,
)
from domain.algo.genetics.elements.mutations.mixed_mutations import (
    inversion_or_swap_mutation,
    inversion_or_swap_or_scramble_mutation,
)
from domain.algo.genetics.elements.mutations.norse_mutation import norse_mutation
from domain.algo.genetics.elements.mutations.scramble_mutation import scramble_mutation
from domain.algo.genetics.elements.mutations.swap_mutation import swap_mutation

mutations = [
    inversion_mutation,
    norse_mutation,
    scramble_mutation,
    swap_mutation,
    inversion_or_swap_mutation,
    inversion_or_swap_or_scramble_mutation,
]
