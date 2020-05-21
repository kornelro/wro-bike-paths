from dataclasses import dataclass
from bike.model.vertex import Vertex


@dataclass(frozen=True)
class Edge:
    id: int
    v1: Vertex
    v2: Vertex
    edge_type: str
    direction: int
    distance: float
