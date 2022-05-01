from models.truck import Truck
from models.truck_path import TruckPath


def compute_total_fitness(dna):
    pass

def index_to_trucks(dna):
    trucks = []
    for truck in dna:
        total_path = []
        for truck_path in truck:
            total_path.append(TruckPath())



def compute_truck_fitness(truck: Truck) -> float:
    fitness = 0
    for path in truck.paths:
        fitness += (path.distance + path.distance * path.money)

    return fitness


def divide_by_truck(dna):
    group2_beginning = dna[-2] + 1
    group3_beginning = dna[-1] + 1

    group1 = dna[1:group2_beginning]
    group2 = dna[group2_beginning:group3_beginning]
    group3 = dna[group3_beginning:-2]

    return group1, group2, group3
