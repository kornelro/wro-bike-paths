from dataclasses import dataclass


@dataclass(frozen=True)
class Vertex:
    id: int
    x: float
    y: float
