import csv
from unittest import TestCase

from models import GlobalConfig, Place
from utils import csv
from domain.compute_fitness import divide_by_truck, index_to_truck
from utils.compute_global_config import get_global_config


class TestFitness(TestCase):
    dna = [0, 3, 1, 2, 4, 7, 9, 6, 8, 5, 3, 7]

    def test_division_by_truck(self):
        division = divide_by_truck(self.dna)
        assert division == [[3, 1, 2], [4, 7, 9, 6], [8, 5]]

    def test_index_to_truck(self):
        truck = index_to_truck([8, 5], get_global_config())
        print(truck.paths)
