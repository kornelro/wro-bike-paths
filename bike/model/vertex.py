from dataclasses import dataclass


@dataclass()
class Vertex:
    id: int
    x: float
    y: float
    roads_vertex_id: int = None
