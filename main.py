from domain.global_config import GlobalConfig
from utils import geo, csv
from utils.geo import Place


def launch():
    global_config = GlobalConfig()
    for name, address in csv.get_rows_from_csv('assets/town_halls.csv'):
        long, lat = geo.search(name, address)
        global_config.add_place(Place(name, long, lat))


