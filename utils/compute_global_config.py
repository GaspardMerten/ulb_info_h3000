from domain import geo
from domain.geo import compute_distance_between_all_places
from models import GlobalConfig, Place
from utils import csv


def get_global_config():
    MONEY_PER_RESIDENT = 0.7

    places = []

    for name, address, population in csv.get_rows_from_csv('../assets/town_halls.csv'):
        long, lat = geo.search(address)

        total_money_in_town_hall = int(population) * MONEY_PER_RESIDENT

        places.append(Place(name, long, lat, total_money_in_town_hall))

    distances_map = compute_distance_between_all_places(places)
    return GlobalConfig(places=places, distances_map=distances_map)
