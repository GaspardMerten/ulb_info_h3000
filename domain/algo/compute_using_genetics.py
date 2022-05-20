from math import inf
from typing import List

from domain.algo.genetics.composable import Composable
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.compute_fitness import (
    compute_total_fitness,
    compute_total_fitness_separated,
)
from domain.dna import (
    generate_random_dna,
)
from models import GlobalConfig, DNA, EnhancedGenerationResult, EnhancedGeneration
from models.algo_result import AlgoResult, TurnResult


def computing_with_genetics_algo(
    config: GlobalConfig, algo_config: GeneticAlgorithmConfig
) -> AlgoResult:
    algo = Composable(
        config=config,
        apply_mutation=algo_config.mutation,
        generate_children_from_parents=algo_config.crossover,
        select_parents=algo_config.selection,
        mutation_rate=algo_config.mutation_rate
    )

    current_generation: List[DNA] = [
        generate_random_dna()
        # algo.get_boosted_dna(generate_random_dna())
        for _ in range(algo_config.number_of_elements_per_generation)
    ]

    bests: List[TurnResult] = []

    previous_best = inf

    for turn in range(algo_config.number_of_generations):
        enhanced_generation = _build_enhanced_generation(current_generation, config)
        current_generation = algo.generate_new_generation(enhanced_generation)

        algo.apply_mutation_to_generation(generation=current_generation)

        fitness = {
            index: compute_total_fitness(dna, config)
            for index, dna in enumerate(current_generation)
        }

        total_fitness = sorted(fitness.values())[0]
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
        final_generation=_build_enhanced_generation_result(current_generation, config),
    )


def _build_enhanced_generation_result(
    generation: List[DNA], config: GlobalConfig
) -> EnhancedGenerationResult:
    return {
        dna: (
            compute_total_fitness(dna, config),
            compute_total_fitness_separated(dna, config),
        )
        for dna in generation
    }


def _build_enhanced_generation(
    generation: List[DNA], config: GlobalConfig
) -> EnhancedGeneration:
    return [(dna, compute_total_fitness(dna, config)) for dna in generation]
