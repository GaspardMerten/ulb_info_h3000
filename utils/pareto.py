from models.typedef import EnhancedGenerationResult


def extract_pareto_from_generation(
    generation: EnhancedGenerationResult,
) -> EnhancedGenerationResult:
    pareto_generation: EnhancedGenerationResult = {}

    for dna, values in generation.items():
        current_dna_fitness_distance, current_dna_fitness_risk = values[1]

        should_add = _is_pareto_optimal(
            current_dna_fitness_distance, current_dna_fitness_risk, generation
        )

        if should_add:
            pareto_generation[dna] = values
    return pareto_generation


def _is_pareto_optimal(
    current_dna_fitness_distance, current_dna_fitness_risk, generation
):
    should_add = True
    for _, fitness_tuple in generation.values():
        if (
            fitness_tuple[0] < current_dna_fitness_distance
            and fitness_tuple[1] < current_dna_fitness_risk
        ):
            should_add = False
            break
    return should_add
