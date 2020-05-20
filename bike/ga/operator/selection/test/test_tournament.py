from evobench.benchmark import Benchmark
from evobench.model import Population
from pytest import fixture

from ..tournament import Tournament


@fixture
def tournament(benchmark: Benchmark) -> Tournament:
    return Tournament(benchmark, pop_size=10, tournament_size=2)


def test_tournament(tournament: Tournament, population: Population):
    new_population = tournament(population)

    assert len(new_population.solutions) < len(population.solutions)
    assert len(new_population.solutions) == tournament.POP_SIZE
