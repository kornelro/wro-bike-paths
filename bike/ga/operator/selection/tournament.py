import random
from typing import List

from evobench.benchmark import Benchmark
from evobench.model import Population, Solution

from .selection import Selection


class Tournament(Selection):

    def __init__(
        self,
        benchmark: Benchmark,
        pop_size: int,
        tournament_size: int
    ):
        super(Tournament, self).__init__(
            benchmark,
            pop_size
        )

        self.TOURNAMENT_SIZE = tournament_size

    def __call__(self, population: Population) -> Solution:
        self.benchmark.evaluate_population(population)
        solutions = population.solutions.copy()

        new_solutions = []

        while(len(new_solutions) < self.POP_SIZE):
            contestants = random.choices(solutions, k=self.TOURNAMENT_SIZE)
            best_solution = self.__tournament(contestants)

            solutions = [
                solution
                for solution in solutions
                if solution.__hash__ != best_solution.__hash__
            ]

            solutions = list(solutions)
            new_solutions.append(best_solution)

        return Population(new_solutions)

    def __tournament(self, solutions: List[Solution]) -> Solution:
        solutions = sorted(solutions, key=lambda solution: solution.fitness)
        return solutions[-1]
