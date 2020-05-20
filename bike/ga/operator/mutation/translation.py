from evobench.benchmark import Benchmark
from evobench.model import Solution
from numpy import random

from .mutation import Mutation


class Translation(Mutation):
    # TODO: tylko dla przykładu, my musimy zaimplementować flipa

    def __init__(
        self,
        benchmark: Benchmark,
        prob: float,
        factor: float,
        gene_prob: float,
    ):
        super(Translation, self).__init__(
            benchmark,
            prob,
            factor
        )

        self.GENE_PROB = gene_prob

    def mutate(self, solution: Solution) -> Solution:

        translation = random.normal(
            scale=self.factor,
            size=self.benchmark.genome_size
        )

        translation *= self.benchmark.bound_range

        prob = random.uniform(size=self.benchmark.genome_size)
        mask = prob < self.GENE_PROB

        genome = solution.genome.copy()
        genome[mask] += translation[mask]

        solution = Solution(genome)

        return self.benchmark.fix(solution)
