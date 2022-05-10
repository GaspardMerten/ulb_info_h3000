from typing import List

from domain.algo.genetics import INaturalSelection
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.compute_fitness import compute_total_fitness, compute_total_fitness_separated
from domain.dna import generate_random_dna, dna_fragment_to_truck, extract_fragments_from_dna
from models import GlobalConfig, DNA
from utils.plot import plot_truck_paths_and_show


def computing_with_genetics_algo(config: GlobalConfig, algo: INaturalSelection, algo_config: GeneticAlgorithmConfig) -> \
        List[DNA]:
    current_generation: List[DNA] = [
        generate_random_dna()
        for _ in range(algo_config.number_of_elements_per_generation)
    ]

    previous_best = 1000

    for turn in range(algo_config.number_of_generations):
        fitness = {
            index: compute_total_fitness(dna, config)
            for index, dna in enumerate(current_generation)
        }

        current_generation = algo.generate_new_generation(current_generation, fitness)

        algo.apply_mutation_to_generation(generation=current_generation)

        best_dna_index = sorted(fitness.items(), key=lambda x: x[1])[0][0]

        current_generation[best_dna_index] = algo.get_boosted_dna(current_generation[best_dna_index], config)

        best_dna = current_generation[best_dna_index]

        if sum(best_dna[1:20]) != 190:
            raise Exception(best_dna)

        total_fitness_separated = compute_total_fitness_separated(best_dna, config)
        total_fitness = compute_total_fitness(best_dna, config)

        if previous_best > total_fitness:
            print('\n' + str(best_dna))
            previous_best = total_fitness
            plot_truck_paths_and_show(trucks=[
                dna_fragment_to_truck(frag, config)
                for frag in extract_fragments_from_dna(best_dna)
            ], title=str(total_fitness_separated) + ' -> ' + str(total_fitness))

        print(f'\rGeneration {turn}/{algo_config.number_of_generations}', end='')

    return current_generation
