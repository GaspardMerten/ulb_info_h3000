import dataclasses
import json
import uuid
import xlsxwriter

from models import GlobalConfig
from models.algo_result import AlgoResult
from utils.plot import plot_algo_result

DEFAULT_PATH = 'results/'


def save_algo_result(result: AlgoResult, config: GlobalConfig, path: str = DEFAULT_PATH, name_builder=uuid.uuid4):
    name = name_builder()
    workbook = xlsxwriter.Workbook(f'{path}{name}.xlsx')

    main = workbook.add_worksheet('Général')

    best = result.results[-1]

    rows = [
        ["Selection", result.config.selection.__name__],
        ["Mutation", result.config.mutation.__name__],
        ["Crossover", result.config.crossover.__name__],
        ["Number of elements per generation", result.config.number_of_elements_per_generation],
        ["Number of generations", result.config.number_of_generations],
        ["Best fitness", best.fitness],
        ["Best fitness distance", best.distance_fitness],
        ["Best fitness risk", best.risk_fitness],
        ["Best DNA", str(best.dna)],
    ]

    for c, i in enumerate(rows):
        main.write_row(c, 0, i)

    results_sheet = workbook.add_worksheet('Results')

    results_sheet.write_row(0, 0,
                            ['DNA', 'Fitness', 'Distance fitness', 'Risk fitness', 'Generation', 'Boost imporvement'])

    for c, r in enumerate(result.results, start=1):
        results_sheet.write_row(c, 0, [str(r.dna), r.fitness, r.distance_fitness, r.risk_fitness, r.generation,
                                       r.boost_improvement])
    last_generation_sheet = workbook.add_worksheet('Dernière gen')

    last_generation_sheet.write_row(0, 0,
                                    ['DNA', 'Fitness', 'Distance fitness', 'Risk fitness'])

    for c, r in enumerate(result.final_generation.items(), start=1):
        last_generation_sheet.write_row(c, 0, [str(r[0]), r[1][0], *r[1][1]])

    workbook.close()

    with open(f"{path}{name}.json", mode="w") as json_file:
        json_file.write(json.dumps(list(result.final_generation.items())))

    plot_algo_result(result, config, name_builder=lambda: name)
