from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics.HGA import HGA
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.algo.genetics.simple import SimpleAlgo
from utils.compute_global_config import get_global_config
from utils.plot import plot_algo_result


def main():
    global_config = get_global_config()

    algo_result = computing_with_genetics_algo(
        global_config,
        GeneticAlgorithmConfig(
            number_of_generations=1000,  # of 20 run, only one had a new best after the 500th generation
            number_of_elements_per_generation=100,
            algo_type=HGA
        )
    )

    plot_algo_result(algo_result, global_config)


if __name__ == '__main__':
    main()
