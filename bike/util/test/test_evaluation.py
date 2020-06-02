from copy import deepcopy

from bike.model.edge import Edge
from bike.model.graph import Graph
from bike.util.evaluation import add_edge
from bike.util.snap import snap_vertices


def test_add_edge_1(graph_bikes: Graph, graph_roads: Graph):

    graph_bikes_snapped = snap_vertices(graph_roads, deepcopy(graph_bikes))

    # krawedz (67, 68), obydwa nowe
    edge = graph_roads.edges[66]
    test_graph = add_edge(graph_bikes_snapped, edge)

    assert len(test_graph.nx_graph.edges) == len(graph_bikes_snapped.nx_graph.edges) + 1
    assert len(test_graph.edges) == len(graph_bikes_snapped.edges) + 1
    assert len(test_graph.nx_graph.nodes) == len(graph_bikes_snapped.nx_graph.nodes) + 2
    assert len(test_graph.vertices) == len(graph_bikes_snapped.vertices) + 2


def test_add_edge_2(graph_bikes: Graph, graph_roads: Graph):

    graph_bikes_snapped = snap_vertices(graph_roads, deepcopy(graph_bikes))

    # krawedz (53, 54), 54 nowy
    edge = graph_roads.edges[51]
    test_graph = add_edge(graph_bikes_snapped, edge)

    assert len(test_graph.nx_graph.edges) == len(graph_bikes_snapped.nx_graph.edges) + 1
    assert len(test_graph.edges) == len(graph_bikes_snapped.edges) + 1
    assert len(test_graph.nx_graph.nodes) == len(graph_bikes_snapped.nx_graph.nodes) + 1
    assert len(test_graph.vertices) == len(graph_bikes_snapped.vertices) + 1


def test_add_edge_3(graph_bikes: Graph, graph_roads: Graph):

    graph_bikes_snapped = snap_vertices(graph_roads, deepcopy(graph_bikes))

    # krawedz (51, 52), obydwa zesnapowane
    edge = Edge(
        id=None,
        v1=graph_roads.vertices_by_id[41],
        v2=graph_roads.vertices_by_id[45]
    )
    test_graph = add_edge(graph_bikes_snapped, edge)

    assert len(test_graph.nx_graph.edges) == len(graph_bikes_snapped.nx_graph.edges) + 1
    assert len(test_graph.edges) == len(graph_bikes_snapped.edges) + 1
    assert len(test_graph.nx_graph.nodes) == len(graph_bikes_snapped.nx_graph.nodes)
    assert len(test_graph.vertices) == len(graph_bikes_snapped.vertices)
