from multiprocessing import Process
from typing import List

from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.algo.genetics.elements.crossover import crossovers
from domain.algo.genetics.elements.mutations import mutations
from domain.algo.genetics.elements.selections import selections
from names import names_of_hundred_bests
from utils.compute_global_config import get_global_config
from utils.save_algo_result import save_algo_result


def process(a, b):
    for c in b:
        try:
            _value = computing_with_genetics_algo(a, c)
            save_algo_result(_value, a)
        except Exception as s:
            print(s)


def compute_configs_from_names(names: List[str]):
    configs = []

    for name in names:
        (
            selection,
            mutation,
            crossover,
            mutation_rate_str,
            nb_of_generation_str,
        ) = name.split("-")
        mutation_rate = float(mutation_rate_str)
        configs.append(
            GeneticAlgorithmConfig(
                number_of_generations=500,
                number_of_elements_per_generation=200,
                selection=[i for i in selections if i.__name__ == selection][0],
                crossover=[i for i in crossovers if i.__name__ == crossover][0],
                mutation=[i for i in mutations if i.__name__ == mutation][0],
                mutation_rate=mutation_rate,
            )
        )
    return configs


def main(config_mode: int):
    global_config = get_global_config()

    threads = []
    if config_mode == 0:
        configs = get_all_configs()
    elif config_mode == 1:
        configs = compute_configs_from_names(names_of_hundred_bests)
    else:
        configs = compute_configs_from_names(
            ["extreme_elitist_sample-inversion_mutation-distance_based_crossover-0.4-0"]
            * 10
        )

    NUMBER_OF_PROCESSES = 10

    for i in range(NUMBER_OF_PROCESSES + 1):
        x = Process(
            target=process,
            args=(
                global_config,
                configs[
                    round(i * (len(configs)) / NUMBER_OF_PROCESSES) : round(
                        (i + 1) * (len(configs)) / NUMBER_OF_PROCESSES
                    )
                ],
            ),
        )
        x.start()
        threads.append(x)

    for thread in threads:
        thread.join()


def get_all_configs():
    configs = []
    for number_of_elements_generations in [100, 200, 300, 400, 500]:
        for mutation_rate in [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]:
            for crossover in crossovers:
                for mutation in mutations:
                    for selection in selections:
                        configs.append(
                            GeneticAlgorithmConfig(
                                number_of_generations=500,
                                number_of_elements_per_generation=number_of_elements_generations,
                                selection=selection,
                                crossover=crossover,
                                mutation=mutation,
                                mutation_rate=mutation_rate,
                            )
                        )
    return configs


if __name__ == "__main__":
    main(2)
