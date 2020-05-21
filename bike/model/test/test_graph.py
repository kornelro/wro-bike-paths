from pytest import fixture
from pathlib import Path
from bike.model.edge import Edge
from bike.model.vertex import Vertex
import networkx as nx

from ..graph import Graph


def test_vertices(graph: Graph):
    vertices = graph.vertices

    assert isinstance(vertices, list)
    assert len(vertices) == 10
    assert all(isinstance(vertex, Vertex) for vertex in vertices)


def test_vertices_by_id(graph: Graph):
    vertices_by_id = graph.vertices_by_id

    assert isinstance(vertices_by_id, dict)
    # TODO


def test_edges(graph: Graph):
    edges = graph.edges

    assert isinstance(edges, list)
    assert len(edges) == 8
    assert all(isinstance(edge, Edge) for edge in edges)


def test_nx_graph(graph: Graph):
    nx_graph = graph.nx_graph

    assert isinstance(nx_graph, nx.Graph)

