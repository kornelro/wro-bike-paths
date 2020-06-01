import math
from dataclasses import dataclass

from lazy_property import LazyProperty

from bike.model.vertex import Vertex


@dataclass()
class Edge:
    id: int
    v1: Vertex
    v2: Vertex

    @LazyProperty
    def distance(self) -> float:
        distance = (self.v2.x - self.v1.x) ** 2 + (self.v2.y - self.v1.y) ** 2
        return math.sqrt(distance)
