from domain import geo
from domain.geo import compute_distance_between_all_places, DistancesMap
from models import GlobalConfig, Place
from utils import csv

MONEY_PER_RESIDENT = 10


def main():
    places = []

    for name, address, population in csv.get_rows_from_csv('assets/town_halls.csv'):
        long, lat = geo.search(address)

        total_money_in_town_hall = population * MONEY_PER_RESIDENT

        places.append(Place(name, long, lat, total_money_in_town_hall))

    distances_map: DistancesMap = compute_distance_between_all_places(places)

    global_config = GlobalConfig(places=places, distances_map=distances_map)


if __name__ == '__main__':
    main()
