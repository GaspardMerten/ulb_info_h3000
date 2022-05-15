from domain import dna as dna_utils
from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics import GeneticAlgorithmConfig
from domain.algo.genetics.HGA import HGA
from domain.algo.genetics.simple import SimpleAlgo
from utils.compute_global_config import get_global_config
from utils.plot import plot_truck_paths_and_show


def main():
    global_config = get_global_config()

    generation = computing_with_genetics_algo(
        global_config,
        HGA(global_config),
        GeneticAlgorithmConfig(
            number_of_generations=500,  # of 20 run, only one had a new best after the 500th generation
            number_of_elements_per_generation=100,
        )
    )

    for i in generation:
        print(i)

    plot_truck_paths_and_show(trucks=[
        dna_utils.dna_fragment_to_truck(frag, global_config)
        for frag in dna_utils.extract_fragments_from_dna(generation[0])
    ])


if __name__ == '__main__':
    main()
