from domain.algo.genetics.elements.crossover.distance_based_crossover import (
    distance_based_crossover,
)
from domain.algo.genetics.elements.crossover.multi_point_crossover import (
    multi_point_crossover,
)
from domain.algo.genetics.elements.crossover.one_point_crossover import (
    one_point_crossover,
)
from domain.algo.genetics.elements.crossover.shuffle_and_swap_crossover import (
    shuffle_and_swap_crossover,
)
from domain.algo.genetics.elements.crossover.uniform_crossover import uniform_crossover

crossovers = [
    distance_based_crossover,
    multi_point_crossover,
    one_point_crossover,
    shuffle_and_swap_crossover,
    uniform_crossover,
]
