from copy import deepcopy

from tqdm.auto import tqdm

from bike.batch import Batch
from bike.stats import BatchStats
from bike.util.plot import Plot


def process(batch: Batch) -> BatchStats:
    plot = Plot()

    population = batch.benchmark.initialize_population(batch.pop_size)
    batch.benchmark.evaluate_population(population)

    population_history = []
    population_history.append(population)

    for _ in tqdm(range(batch.epochs), desc='Epochs'):
        for operator in batch.pipeline:
            population = operator(population)

        batch.benchmark.evaluate_population(population)
        population_history.append(deepcopy(population))

    # ? TODO: tu mogą być problemy z pamięcią, raczej będziemy mieć dużą sieć
    stats = BatchStats(population_history)
    plot.ga_convergence(stats)

    return stats
