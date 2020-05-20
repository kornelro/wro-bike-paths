from abc import abstractmethod

from evobench.benchmark import Benchmark
from evobench.model import Population
from abc import ABC


class Operator(ABC):

    def __init__(self, benchmark: Benchmark):
        super(Operator, self).__init__()

        self.benchmark = benchmark

    @abstractmethod
    def __call__(self, population: Population) -> Population:
        pass
