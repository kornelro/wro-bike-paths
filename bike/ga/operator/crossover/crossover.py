import itertools
import random
from abc import abstractmethod
from typing import Tuple

import numpy as np
from evobench.benchmark import Benchmark
from evobench.model import Population, Solution

from bike.ga.operator.operator import Operator


class Crossover(Operator):

    def __init__(
        self,
        benchmark: Benchmark,
        prob: float,
    ):
        super(Crossover, self).__init__(benchmark)

        self.PROB = prob

    def __call__(self, population: Population) -> Population:
        solutions = population.solutions.copy()
        random.shuffle(solutions)

        pairs = zip(population.solutions, solutions)
        pairs = list(pairs)
        pairs = np.array(pairs)

        mask = np.random.uniform(size=len(pairs))
        mask = mask < self.PROB
        pairs = pairs[mask]

        offsprings = itertools.starmap(self.cross, pairs)

        offsprings = itertools.chain.from_iterable(offsprings)
        offsprings = list(offsprings)

        solutions = population.solutions + offsprings
        random.shuffle(solutions)

        return Population(solutions)

    @abstractmethod
    def cross(self, a: Solution, b: Solution) -> Tuple[Solution, Solution]:
        pass
