from typing import Tuple

import numpy as np
from evobench.benchmark import Benchmark
from evobench.model import Solution
from numpy import random

from .crossover import Crossover


class Swap(Crossover):

    def __init__(
        self,
        benchmark: Benchmark,
        prob: float,
        width_prob: float
    ):
        super(Swap, self).__init__(
            benchmark,
            prob
        )

        self.WIDTH_PROB = width_prob

    def cross(self, a: Solution, b: Solution) -> Tuple[Solution, Solution]:
        mask = random.uniform(size=self.benchmark.genome_size)
        mask = mask < self.WIDTH_PROB

        return self.__swap(a, b, mask)

    def __swap(
        self,
        a: Solution,
        b: Solution,
        mask: np.ndarray
    ) -> Tuple[Solution, Solution]:

        new_a = a.genome.copy()
        new_a[mask] = b.genome[mask]

        new_b = b.genome.copy()
        new_b[mask] = a.genome[mask]

        return Solution(new_a), Solution(new_b)
