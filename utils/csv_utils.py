import csv


def get_rows_from_csv(file_name: str):
    addresses = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            addresses.append(row)

    return addresses
