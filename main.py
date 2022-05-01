from models.truck import Truck
from models.truck_path import TruckPath
from utils import geo, csv
from utils.plot import plot_truck_paths_and_show, plot_truck_paths_and_places

lat_long_for_town_halls = []

for name, address in csv.get_rows_from_csv('assets/town_halls.csv'):
    lat_long_for_town_halls.append(geo.search(name, address))

trucks = [
    Truck(
        paths=[
            TruckPath(
                origin=t,
                destination=lat_long_for_town_halls[index + 1],
                distance=0,
                money=index
            )
            for index, t in enumerate(lat_long_for_town_halls[:5])
        ],
    ),
]


exit()
distance_dict = {}

for index, lat_long_1 in enumerate(lat_long_for_town_halls):
    for lat_long_2 in lat_long_for_town_halls[index + 1:]:
        distance_dict[(lat_long_1, lat_long_2)] = geo.get_time_between(lat_long_1, lat_long_2)
        distance_dict[(lat_long_2, lat_long_1)] = geo.get_time_between(lat_long_2, lat_long_1)
