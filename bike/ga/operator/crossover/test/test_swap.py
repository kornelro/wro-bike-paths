from evobench.benchmark import Benchmark
from evobench.model import Population
from pytest import fixture

from ..swap import Swap


@fixture
def swap(benchmark: Benchmark) -> Swap:
    return Swap(
        benchmark,
        prob=0.5,
        width_prob=0.3
    )


def test_swap(swap: Swap, population: Population):
    new_population = swap(population)

    assert len(population.solutions) < len(new_population.solutions)
