from pathlib import Path
from typing import Dict

import numpy as np
from evobench.benchmark import Benchmark as Base
from evobench.model import Population, Solution
from lazy import lazy


class Benchmark(Base):

    def __init__(
        self,
        graph_path: Path,
        multiprocessing: bool = False
    ):
        """
        Wrapper for _CEC2013LSGO_ problems.

        Parameters
        ----------
        problem_id : int
            ID of the problem. Problems can be found at cec2013lsgo paper.
        """

        # TODO: random seed

        super(Benchmark, self).__init__(
            shuffle=False,
            multiprocessing=multiprocessing
        )

        self.GRAPH_PATH = graph_path
        # TODO: wczytywanie grafu

    @lazy
    def global_opt(self) -> float:
        # ? tego nie znamy
        pass

    @lazy
    def genome_size(self) -> int:
        # TODO
        pass

    @lazy
    def lower_bound(self) -> np.ndarray:
        # niepotrzebne
        pass

    @lazy
    def upper_bound(self) -> np.ndarray:
        # niepotrzebne
        pass

    @lazy
    def bound_range(self) -> np.ndarray:
        # niepotrzebne
        pass

    @lazy
    def as_dict(self) -> Dict:
        # TODO: parametry problemu, żebyśmy później orientowali się w logach
        as_dict = {}
        as_dict['graph_path'] = self.GRAPH_PATH

        return as_dict

    def random_solution(self) -> Solution:
        genome = np.random.randint(low=0, high=2, dtype=np.bool)
        return Solution(genome)

    def initialize_population(self, size: int) -> Population:
        size = int(size)
        solutions = []

        for _ in range(size):
            genome = self.random_solution().genome

            solution = Solution(genome)
            solutions.append(solution)

        return Population(solutions)

    def _evaluate_solution(self, solution: Solution) -> float:
        # TODO: zdekodować genotyp do fenotypu, odpalić metryczkę z networkx
        pass
