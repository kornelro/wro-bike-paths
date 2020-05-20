from abc import abstractmethod

from evobench.benchmark import Benchmark
from evobench.model import Population, Solution

from bike.ga.operator.operator import Operator
import numpy as np
import random


class Mutation(Operator):

    def __init__(
        self,
        benchmark: Benchmark,
        prob: float,
        factor: float
    ):
        super(Mutation, self).__init__(benchmark)

        self.PROB = prob
        self.INIT_FACTOR = factor
        self.factor = factor

    def __call__(self, population: Population) -> Population:
        solutions = population.solutions.copy()
        solutions = np.array(solutions)

        mask = np.random.uniform(size=len(solutions))
        mask = mask < self.PROB

        solutions = solutions[mask]
        solutions = map(self.mutate, solutions)
        solutions = list(solutions)

        solutions += population.solutions
        random.shuffle(solutions)

        return Population(solutions)

    def reset_factor(self):
        self.factor = self.INIT_FACTOR

    @abstractmethod
    def mutate(self, solution: Solution) -> Solution:
        pass
