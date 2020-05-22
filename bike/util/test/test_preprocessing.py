import networkx as nx

from bike.model.graph import Graph
from bike.util.preprocessing import smooth_graph


def test_smooth_graph(graph: Graph):
    nx_graph = smooth_graph(graph, 45)

    assert isinstance(nx_graph, nx.Graph)
