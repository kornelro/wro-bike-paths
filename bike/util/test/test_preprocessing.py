from bike.model.graph import Graph
from bike.util.preprocessing import smooth_graph, remove_snapped, update_edges


def test_smooth_graph(graph_bikes: Graph):
    nx_graph = smooth_graph(graph_bikes, 45)

    assert isinstance(nx_graph, Graph)


def test_removed_snapped(graph_roads: Graph):
    graph_roads = remove_snapped(graph_roads, [0, 1])

    assert len(graph_roads.nx_graph.edges) == 66


def test_update_edges(graph_roads: Graph):
    graph_roads.nx_graph.remove_edge(0, 1)
    graph_roads.nx_graph.remove_edge(1, 2)

    assert len(graph_roads.edges) != len(graph_roads.nx_graph.edges)

    prev_len = len(graph_roads.edges)
    graph_roads = update_edges(graph_roads)

    assert len(graph_roads.edges) == len(graph_roads.nx_graph.edges)
    assert len(graph_roads.edges) < prev_len


