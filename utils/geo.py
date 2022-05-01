import urllib.parse
from dataclasses import dataclass

import requests

OSM_ROUTING_DOMAIN = "routing.openstreetmap.de"
OSM_NOMINATIM_DOMAIN = "nominatim.openstreetmap.org"

OSM_ROUTING_URL = f"https://{OSM_ROUTING_DOMAIN}/routed-car/route/v1/driving/"
OSM_NOMINATIM_URL = f"https://{OSM_NOMINATIM_DOMAIN}/search/"


@dataclass
class LatLong:
    lat: int
    long: int


def search(search_string) -> [float, float]:
    quoted_search_string = urllib.parse.quote(search_string)
    search_url = f"{OSM_NOMINATIM_URL}?q={quoted_search_string}&limit=1&format=json&addressdetails=1"

    response = requests.get(search_url)
    response_json = response.json()

    if not response_json:
        raise Exception(f"Could not find result for {search_string}")

    address_dict = response_json[0]

    return LatLong(lat=address_dict['lat'], long=address_dict['lon'])


def get_time_between(origin: LatLong, destination: LatLong) -> int:
    time_url = f'{OSM_ROUTING_URL}{origin.lat},{origin.long}/{destination.lat},{destination.long}'
    time_url_with_parameters = f'{time_url}?overview=false&alternatives=false&steps=false'

    response = requests.get(time_url_with_parameters)
    response_json = response.json()

    if not response_json:
        raise Exception(f"Could not find time between {origin} and {destination}")

    return response_json['routes'][0]['duration']