from typing import List

from domain.algo.genetics import INaturalSelection
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.compute_fitness import compute_total_fitness
from domain.dna import _generate_random_dna
from models import GlobalConfig, DNA


def computing_with_genetics_algo(config: GlobalConfig, algo: INaturalSelection, algo_config: GeneticAlgorithmConfig):
    current_generation: List[DNA] = [
        _generate_random_dna()
        for _ in range(algo_config.number_of_elements)
    ]

    fitness = [
        compute_total_fitness(dna)
        for dna in current_generation
    ]

    print(fitness)
