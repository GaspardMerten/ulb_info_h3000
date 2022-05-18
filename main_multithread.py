from multiprocessing import Process

from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics.config import GeneticAlgorithmConfig
from domain.algo.genetics.elements.crossover import crossovers
from domain.algo.genetics.elements.mutations import mutations
from domain.algo.genetics.elements.selections import selections
from utils.compute_global_config import get_global_config
from utils.save_algo_result import save_algo_result


def process(a, b):
    for c in b:
        try:
            _value = computing_with_genetics_algo(a, c)
            save_algo_result(_value, a)
        except Exception as s:
            print(s)
def main():
    global_config = get_global_config()

    threads = []
    configs = []

    for crossover in crossovers:
        for mutation in mutations:
            for selection in selections:
                configs.append(
                    GeneticAlgorithmConfig(
                        number_of_generations=500,
                        number_of_elements_per_generation=100,
                        selection=selection,
                        crossover=crossover,
                        mutation=mutation,
                    )
                )

    NUMBER_OF_PROCESSES = 10

    for i in range(NUMBER_OF_PROCESSES + 1):
        print(round(i * (len(configs)) / NUMBER_OF_PROCESSES), round(
            (i + 1) * (len(configs)) / NUMBER_OF_PROCESSES
        ))
        x = Process(
            target=process,
            args=(
                global_config,
                configs[
                round(i * (len(configs)) / NUMBER_OF_PROCESSES): round(
                    (i + 1) * (len(configs)) / NUMBER_OF_PROCESSES
                )
                ],
            ),
        )
        x.start()

        print(f"thread {i}")

        threads.append(x)

    for thread in threads:
        print("Joining thread")
        thread.join()


if __name__ == "__main__":
    main()
