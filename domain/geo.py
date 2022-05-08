import urllib.parse
import urllib.parse
from typing import List

import requests
from diskcache import Cache

from models import Place, DistancesMap

__all__ = ('get_distance_between', 'search', 'compute_distance_between_all_places')

cache = Cache("cache")

OSM_ROUTING_DOMAIN = "routing.openstreetmap.de"
OSM_NOMINATIM_DOMAIN = "nominatim.openstreetmap.org"

OSM_ROUTING_URL = f"https://{OSM_ROUTING_DOMAIN}/routed-car/route/v1/driving/"
OSM_NOMINATIM_URL = f"https://{OSM_NOMINATIM_DOMAIN}/search/"


@cache.memoize()
def search(search_string) -> [float, float]:
    quoted_search_string = urllib.parse.quote(search_string)
    search_url = f"{OSM_NOMINATIM_URL}?q={quoted_search_string}&limit=1&format=json&addressdetails=1&country=Belgique&city=Bruxelles"

    response = requests.get(search_url)
    response_json = response.json()

    if not response_json:
        raise Exception(f"Could not find result for {search_string}")

    address_dict = response_json[0]

    return float(address_dict['lat']), float(address_dict['lon'])


@cache.memoize()
def get_distance_between(origin: Place, destination: Place) -> float:
    time_url = f'{OSM_ROUTING_URL}{origin.long},{origin.lat};{destination.long},{destination.lat}'
    time_url_with_parameters = f'{time_url}?overview=false&alternatives=false&steps=false'

    response = requests.get(time_url_with_parameters)
    response_json = response.json()

    if not response_json:
        raise Exception(f"Could not find time between {origin} and {destination}")

    return response_json['routes'][0]['distance']


@cache.memoize()
def compute_distance_between_all_places(places: List[Place]) -> DistancesMap:
    results: DistancesMap = {}

    for count, place_one in enumerate(places):
        for place_two in places:
            if place_one != place_two:
                results[(place_one, place_two)] = get_distance_between(place_one, place_two)

    return results
