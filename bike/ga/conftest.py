from evobench.benchmark import Benchmark
from evobench.discrete.trap import Trap
from evobench.model import Population
from pytest import fixture

__POP_SIZE = 20


@fixture(scope='session')
def benchmark() -> Benchmark:
    # TODO: malutką sieć i testować na naszym problemie
    return Trap(blocks=[10])


@fixture(scope='session')
def population(benchmark: Benchmark) -> Population:
    return benchmark.initialize_population(size=__POP_SIZE)
