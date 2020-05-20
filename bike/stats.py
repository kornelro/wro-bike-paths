from dataclasses import dataclass
from typing import List

import numpy as np
from evobench.model import Population
from lazy import lazy


@dataclass(frozen=True)
class BatchStats:
    population_history: List[Population]

    @lazy
    def fitness_history(self) -> List[np.ndarray]:
        return [population.fitness for population in self.population_history]

    @lazy
    def avg_fitness(self) -> List[float]:
        avg_fitness = [np.average(fitness) for fitness in self.fitness_history]
        return list(avg_fitness)

    @lazy
    def max_fitness(self) -> List[float]:
        max_fitness = [np.max(fitness) for fitness in self.fitness_history]
        return list(max_fitness)

    @lazy
    def min_fitness(self) -> List[float]:
        min_fitness = [np.min(fitness) for fitness in self.fitness_history]
        return list(min_fitness)
