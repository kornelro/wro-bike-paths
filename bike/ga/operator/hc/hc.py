from abc import abstractmethod
from random import random

from evobench.benchmark import Benchmark
from evobench.model import Population, Solution

from ..operator import Operator


class HillClimbing(Operator):

    def __init__(self, probability: float, benchmark: Benchmark):
        self.probability = probability
        self.benchmark = benchmark

    def apply(self, population: Population) -> Population:

        samples = []

        for sample in population.solutions:

            samples.append(sample)

            if random() > self.probability:
                continue

            improved_sample = self.climb(sample)
            samples.append(improved_sample)

        return Population(tuple(samples))

    @abstractmethod
    def climb(self, sample: Solution) -> Solution:
        pass
