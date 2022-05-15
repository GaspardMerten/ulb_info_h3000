from unittest import TestCase
from domain.algo.genetics.HGA import HGA
from models import DNA
from utils.compute_global_config import get_global_config


class TestHGAAlgo(TestCase):
    def test_hga(self):
        hga = HGA(get_global_config("../assets/town_halls.csv"))
        print(hga.generate_children_from_parents(
            (0, 1, 2, 13, 4, 5, 16, 7, 9, 8, 10, 11, 12, 3, 14, 15, 6, 17, 18, 19, 6, 8),
            (0, 4, 1, 3, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 9))
        )

