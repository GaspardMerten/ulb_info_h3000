from domain import geo
from domain.geo import compute_distance_between_all_places, DistancesMap
from models import GlobalConfig, Place
from utils import csv
from utils.compute_global_config import get_global_config


def main():

    global_config = get_global_config()
    print(compute_total_fitness([0, 3, 1, 2, 4, 7, 9, 6, 8, 5, 3, 7], global_config))


if __name__ == '__main__':
    main()
