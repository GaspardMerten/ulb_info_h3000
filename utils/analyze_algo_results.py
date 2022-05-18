import json
from os import listdir
from os.path import join

from matplotlib import pyplot as plt
from openpyxl import load_workbook

from utils.plot import extract_and_plot_pareto_on_graph


def _load_data(folder: str = '../results'):
    name_fitness = {}

    for file_name in listdir(folder):
        if '.xlsx' in file_name:
            file_path = join(folder, file_name)

            try:
                wb = load_workbook(filename=file_path)

                name_fitness[file_name] = wb['Général']['B6'].value

                with open(file_path.replace('.xlsx', '.json')) as json_file:
                    data = json.loads(json_file.read())

                enhanced_generation = {
                    tuple(a[0]): a[1] for a in data
                }

                extract_and_plot_pareto_on_graph(plt, enhanced_generation)
                plt.show()

            except PermissionError:
                pass

    return list(map(lambda x: x[0], sorted(name_fitness.items(), key=lambda x: x[1])))


if __name__ == '__main__':
    print(_load_data()[0])
