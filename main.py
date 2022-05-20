from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.algo.genetics.elements.crossover import crossovers
from domain.algo.genetics.elements.mutations import mutations
from domain.algo.genetics.elements.selections import selections
from utils.compute_global_config import get_global_config
from utils.save_algo_result import save_algo_result


def main():
    global_config = get_global_config()

    algo_variants = len(crossovers) * len(mutations) * len(selections)

    print(f"Number of algorithms to try: {algo_variants}")

    current_variant_count = 0

    for crossover in crossovers:
        for mutation in mutations:
            for selection in selections:
                print(f"Algo: ${crossover.__name__}-{mutation.__name__}-{selection.__name__}")
                for _ in range(1):
                    algo_result = computing_with_genetics_algo(
                        global_config,
                        GeneticAlgorithmConfig(
                            number_of_generations=10000,
                            # out of 20 run, only one had a new best after the 500th generation
                            number_of_elements_per_generation=100,
                            selection=selection,
                            crossover=crossover,
                            mutation=mutation,
                        )
                    )

                    save_algo_result(algo_result, global_config)

                print(f"Algo number {current_variant_count}")
                current_variant_count += 1


if __name__ == '__main__':
    main()
