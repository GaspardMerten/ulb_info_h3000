import csv


def get_all_addresses():
    addresses = []
    with open('communes.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            addresses.append(row[1])

    return addresses

