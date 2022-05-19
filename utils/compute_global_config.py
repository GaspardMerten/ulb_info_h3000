from domain import geo
from domain.geo import compute_distance_between_all_places
from models import GlobalConfig, Place
from utils import csv_utils


def get_global_config(asset_file: str = "assets/town_halls.csv"):
    MONEY_PER_RESIDENT = 0.7

    places = []

    for name, address, population in csv_utils.get_rows_from_csv(asset_file):
        long, lat = geo.search(address)

        total_money_in_town_hall = int(population) * MONEY_PER_RESIDENT

        places.append(Place(name, long, lat, total_money_in_town_hall))

        print(f"Fetched ${address}")

    distances_map = compute_distance_between_all_places(places)
    return GlobalConfig(places=places, distances_map=distances_map)
