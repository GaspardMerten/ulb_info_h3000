from domain.algo.compute_using_genetics import computing_with_genetics_algo
from domain.algo.genetics import GeneticAlgorithmConfig
from domain.algo.genetics.simple import SimpleAlgo
from domain.compute_fitness import compute_total_fitness
from utils.compute_global_config import get_global_config


def main():

    global_config = get_global_config()
    print(compute_total_fitness([0, 3, 1, 2, 4, 7, 9, 6, 8, 5, 3, 7], global_config))
    computing_with_genetics_algo(global_config, SimpleAlgo(), GeneticAlgorithmConfig(number_of_generations=1000, number_of_elements_per_generation=20))

if __name__ == '__main__':
    main()
