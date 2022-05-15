from multiprocessing import Process, Manager

from domain import dna as dna_utils
from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics import GeneticAlgorithmConfig
from domain.algo.genetics.simple import SimpleAlgo
from domain.compute_fitness import compute_total_fitness
from utils.compute_global_config import get_global_config
from utils.plot import plot_truck_paths_and_places


def process(a, b, c, d: list):
    _value = computing_with_genetics_algo(
        a, b, c
    )

    for v in _value:
        d.append(v)


def main():
    global_config = get_global_config()

    threads = []
    manager = Manager()
    generations = manager.list()

    for i in range(100):
        x = Process(
            target=process,
            args=(
                global_config,
                SimpleAlgo(global_config),
                GeneticAlgorithmConfig(
                    number_of_generations=1000,
                    number_of_elements_per_generation=100,
                ),
                generations
            )
        )
        x.start()

        print(f"thread {i}")

        threads.append(x)

    for thread in threads:
        print("Joining thread")
        thread.join()

    for i in generations:
        print(i)

    fitness = {
        index: compute_total_fitness(dna, global_config)
        for index, dna in enumerate(generations)
    }

    best = sorted(fitness.values())[0]

    dna = None

    for index, value in fitness.items():
        if value == best:
            dna = generations[index]

    plot_truck_paths_and_places(
        trucks=[
            dna_utils.dna_fragment_to_truck(frag, global_config)
            for frag in dna_utils.extract_fragments_from_dna(dna)
        ],
        places=global_config.places,
        title=f"Best of 50*100*100 : {best}"
    )


if __name__ == "__main__":
    main()
