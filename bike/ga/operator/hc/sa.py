import math
from typing import List, Tuple

import numpy as np
from evobench.model import Solution

from bike.ga.benchmark import Benchmark
from bike.ga.operator.mutation.mutation import Mutation

from .hc import HillClimber


class SimulatedAnnealing(HillClimber):

    def __init__(
        self,
        benchmark: Benchmark,
        mutation: Mutation,
        t_init: float,
        t_final: float,
        k: float,
        c: float
    ):
        super(SimulatedAnnealing, self).__init__(benchmark)

        self.mutation = mutation
        self.T_INIT = t_init
        self.T_FINAL = t_final
        self.K = k
        self.C = c

    def __call__(
        self,
        solution: Solution
    ) -> Tuple[Solution, List[float], List[float]]:

        fitness = self.benchmark.evaluate_solution(solution)

        convergence = [fitness]
        history = [fitness]

        best_solution = solution
        best_fitness = fitness

        t = self.T_INIT

        while(t > self.T_FINAL):
            self.mutation.factor = self.mutation.INIT_FACTOR * t

            new_solution = self.mutation(solution)
            new_fitness = self.benchmark.evaluate_solution(new_solution)

            history.append(new_fitness)

            if fitness > best_fitness:
                best_fitness = fitness
                best_solution = best_solution

            if new_fitness > fitness:
                solution = new_solution
                fitness = new_fitness
            else:
                df = new_fitness - fitness
                r = np.random.uniform()

                anneal = math.exp(df * self.K * t)

                if anneal < r:
                    solution = new_solution
                    fitness = new_fitness

            t *= self.C
            convergence.append(fitness)

            self.mutation.reset_factor()

        return best_solution, convergence, history
