from bike.model.graph import Graph
from bike.util.snap import snap_vertices, get_snapped_ids
from copy import deepcopy

def test_snap_vertices(graph_roads: Graph, graph_bikes: Graph):
    graph_bikes_snapped = snap_vertices(graph_roads, deepcopy(graph_bikes))
    ids = get_snapped_ids(graph_bikes_snapped)

    assert isinstance(graph_bikes_snapped, Graph)
    assert graph_bikes.vertices_by_id[0].x != graph_bikes_snapped.vertices_by_id[0].x
    assert graph_bikes_snapped.vertices_by_id[0].roads_vertex_id
    assert len(ids) > 0
