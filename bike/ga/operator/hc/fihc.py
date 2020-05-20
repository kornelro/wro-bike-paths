import numpy as np
from evobench import Benchmark
from evobench.model import Solution

from .hc import HillClimbing


class FIHC(HillClimbing):

    def __init__(self, probability: float, benchmark: Benchmark):
        super().__init__(probability, benchmark)

    def climb(self, solution: Solution) -> Solution:
        loci = np.copy(solution.genome)
        loci_order = np.arange(start=0, stop=loci.size)
        np.random.shuffle(loci_order)

        improved_score = self.benchmark.evaluate_solution(solution)
        loci_improved = True

        while loci_improved:

            loci_improved = False

            for index in loci_order:
                loci[index] = not loci[index]
                solution = Solution(loci)
                loci_score = self.benchmark.evaluate_solution(solution)

                if loci_score > improved_score:
                    improved_score = loci_score
                    loci_improved = True
                else:
                    loci[index] = not loci[index]

        return Solution(loci)
