from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics.HGAXSIMPLE import HGAXSimple
from domain.algo.genetics.composable import Composable
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.algo.genetics.elements.selections.elitist import extreme_elitist_sample
from utils.compute_global_config import get_global_config
from utils.save_algo_result import save_algo_result


def main():
    global_config = get_global_config()

    for _ in range(1):
        algo_result = computing_with_genetics_algo(
            global_config,
            GeneticAlgorithmConfig(
                number_of_generations=50,  # of 20 run, only one had a new best after the 500th generation
                number_of_elements_per_generation=100,
                algo_type=lambda x : Composable(
                    config=x,
                    select_parents=extreme_elitist_sample
                )
            )
        )

        save_algo_result(algo_result, global_config)


if __name__ == '__main__':
    main()
