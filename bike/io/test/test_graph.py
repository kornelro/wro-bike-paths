from pytest import fixture
from pathlib import Path
from bike.model.edge import Edge
from bike.model.vertex import Vertex

from ..graph import Graph


def test_vertices(graph: Graph):
    vertices = graph.vertices

    assert isinstance(vertices, list)
    assert len(vertices) == 10
    assert all(isinstance(vertex, Vertex) for vertex in vertices)


def test_edges(graph: Graph):
    edges = graph.edges

    assert isinstance(edges, list)
    assert len(edges) == 8
    assert all(isinstance(edge, Edge) for edge in edges)
