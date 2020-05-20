from dataclasses import dataclass
from typing import List

from lazy import lazy

from bike.ga.benchmark import Benchmark
from bike.ga.operator.operator import Operator


@dataclass
class Batch:
    benchmark: Benchmark
    pop_size: int
    epochs: int
    pipeline: List[Operator]

    @lazy
    def as_dict(self) -> dict:
        as_dict = {}

        as_dict['benchmark'] = self.benchmark.as_dict
        as_dict['pop_size'] = self.pop_size
        as_dict['epochs'] = self.epochs

        # TODO: przelecieć po operatorach i wyciągnać z nich as_dict
        # as_dict['pipeline'] =

        return as_dict
