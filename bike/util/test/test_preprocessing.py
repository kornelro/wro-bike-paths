from bike.model.graph import Graph
from bike.util.preprocessing import smooth_graph


def test_smooth_graph(graph: Graph):
    nx_graph = graph.nx_graph
    nodes = graph.vertices_by_id

    nx_graph = smooth_graph(nx_graph, nodes, 135.)

    assert nx_graph
