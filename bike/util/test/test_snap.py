from bike.model.graph import Graph
from bike.util.snap import snap_vertices


def test_snap_vertices(graph_roads: Graph, graph_bikes: Graph):
    graph_bikes = snap_vertices(graph_roads, graph_bikes)

    assert isinstance(graph_bikes, Graph)
