from unittest import TestCase

from domain.algo.genetics.HGA import HGA
from domain.compute_fitness import divide_by_truck, dna_fragment_to_truck
from utils.compute_global_config import get_global_config


class TestHGAAlgo(TestCase):
    dna = [0, 3, 1, 2, 4, 7, 9, 6, 8, 5, 3, 7]

    def test_hga(self):
        hga = HGA(get_global_config())
        print(hga.hga_algo([0, 1, 2, 3, 4, 5], [0, 5, 3, 2, 4, 1]))
