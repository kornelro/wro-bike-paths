import networkx as nx

from bike.model.graph import Graph
from bike.util.preprocessing import smooth_graph


def test_smooth_graph(graph_bikes: Graph):
    nx_graph = smooth_graph(graph_bikes, 45)

    assert isinstance(nx_graph, nx.Graph)
