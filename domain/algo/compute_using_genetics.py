from math import inf
from typing import List

from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.compute_fitness import (
    compute_total_fitness,
    compute_total_fitness_separated,
)
from domain.dna import (
    generate_random_dna,
    dna_fragment_to_truck,
    extract_fragments_from_dna,
)
from models import GlobalConfig, DNA
from models.algo_result import AlgoResult, TurnResult
from utils.plot import plot_truck_paths_and_places


def computing_with_genetics_algo(
    config: GlobalConfig, algo_config: GeneticAlgorithmConfig
) -> AlgoResult:
    algo = algo_config.algo_type(config)

    current_generation: List[DNA] = [
        generate_random_dna()
        # algo.get_boosted_dna(generate_random_dna())
        for _ in range(algo_config.number_of_elements_per_generation)
    ]

    bests: List[TurnResult] = []

    previous_best = inf

    for turn in range(algo_config.number_of_generations):
        fitness = {
            index: compute_total_fitness(dna, config)
            for index, dna in enumerate(current_generation)
        }
        current_generation = algo.generate_new_generation(current_generation, fitness)

        algo.apply_mutation_to_generation(generation=current_generation)

        fitness = {
            index: compute_total_fitness(dna, config)
            for index, dna in enumerate(current_generation)
        }

        total_fitness = sorted(fitness.values())[0]
        print("MAX VALUE: " + str(total_fitness))
        best_dna_index = None

        for x, v in fitness.items():
            if v == total_fitness:
                best_dna_index = x

        best_dna = current_generation[best_dna_index]

        assert (
            sum(best_dna[1:20]) == 190 and len(best_dna) == 22
        ), f"Incorrect DNA produced: {best_dna}"

        if previous_best > total_fitness:

            print(f"\nNew best {best_dna}\n")
            boosted_dna, improvement_percentage = algo.get_boosted_dna(
                current_generation[best_dna_index]
            )
            if boosted_dna != best_dna:
                current_generation[best_dna_index] = boosted_dna
                total_fitness = compute_total_fitness(best_dna, config)
                best_dna = current_generation[best_dna_index]

            total_fitness_separated = compute_total_fitness_separated(best_dna, config)

            bests.append(
                TurnResult(
                    fitness=total_fitness,
                    risk_fitness=total_fitness_separated[1],
                    distance_fitness=total_fitness_separated[0],
                    dna=best_dna,
                    generation=turn,
                    boost_improvement=improvement_percentage,
                )
            )

            previous_best = total_fitness

        print(
            f"\rGeneration {turn}/{algo_config.number_of_generations} {len(current_generation)} {len(set(current_generation))}, \nTotal fitness:  {total_fitness}",
            end="",
        )

    return AlgoResult(
        results=bests,
        config=algo_config,
        algo=type(algo),
        final_generation={
            dna: (
                compute_total_fitness(dna, config),
                compute_total_fitness_separated(dna, config),
            )
            for dna in current_generation
        },
    )
