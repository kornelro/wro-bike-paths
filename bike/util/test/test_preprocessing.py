from bike.model.graph import Graph
from bike.util.preprocessing import smooth_graph, remove_snapped


def test_smooth_graph(graph_bikes: Graph):
    nx_graph = smooth_graph(graph_bikes, 45)

    assert isinstance(nx_graph, Graph)


def test_removed_snapped(graph_roads: Graph):
    graph_roads = remove_snapped(graph_roads, [0, 1])

    assert len(graph_roads.nx_graph.edges) == 66
