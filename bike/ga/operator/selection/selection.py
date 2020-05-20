from abc import abstractmethod

from evobench.benchmark import Benchmark
from evobench.model import Population

from bike.ga.operator.operator import Operator


class Selection(Operator):

    def __init__(
        self,
        benchmark: Benchmark,
        pop_size: int
    ):
        super(Selection, self).__init__(benchmark)

        self.POP_SIZE = pop_size

    @abstractmethod
    def __call__(self, population: Population) -> Population:
        pass
