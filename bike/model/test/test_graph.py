import networkx as nx

from bike.model.edge import Edge
from bike.model.vertex import Vertex

from ..graph import Graph


def test_vertices(graph_bikes: Graph):
    vertices = graph_bikes.vertices

    assert isinstance(vertices, list)
    assert len(vertices) == 22
    assert all(isinstance(vertex, Vertex) for vertex in vertices)


def test_vertices_by_id(graph_bikes: Graph):
    vertices_by_id = graph_bikes.vertices_by_id

    assert isinstance(vertices_by_id, dict)
    # TODO


def test_edges(graph_bikes: Graph):
    edges = graph_bikes.edges

    assert isinstance(edges, list)
    assert len(edges) == 21
    assert all(isinstance(edge, Edge) for edge in edges)


def test_nx_graph(graph_bikes: Graph):
    nx_graph = graph_bikes.nx_graph

    assert isinstance(nx_graph, nx.Graph)
