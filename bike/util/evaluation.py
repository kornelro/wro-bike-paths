from copy import deepcopy

from bike.model.edge import Edge
from bike.model.graph import Graph
from bike.model.vertex import Vertex


def add_edge(
    bikes: Graph,
    road_edge: Edge
) -> Graph:

    bikes = deepcopy(bikes)

    v1_roads = road_edge.v1
    v2_roads = road_edge.v2

    v1_bikes = None
    v2_bikes = None

    # sprawdzamy czy v z roads maja zesnapowane odpowiedniki w bikes
    for bikes_vertex in bikes.vertices:
        if bikes_vertex.roads_vertex_id == v1_roads.id:
            v1_bikes = bikes.vertices_by_id[bikes_vertex.id]
        elif bikes_vertex.roads_vertex_id == v2_roads.id:
            v2_bikes = bikes.vertices_by_id[bikes_vertex.id]

    # jezeli ktorys nie ma odpowiednika do dodajemy nowy wierzcholek
    # zapisujemy w nim id z roads
    if not v1_bikes:

        v1_bikes = Vertex(
            id=len(bikes.vertices)+1,
            x=v1_roads.x,
            y=v1_roads.y,
            roads_vertex_id=v1_roads.id
        )

        bikes.vertices.append(v1_bikes)
        bikes.vertices_by_id[v1_bikes.id] = v1_bikes
        bikes.nx_graph.add_node(v1_bikes.id)

    if not v2_bikes:

        v2_bikes = Vertex(
            id=len(bikes.vertices)+1,
            x=v2_roads.x,
            y=v2_roads.y,
            roads_vertex_id=v2_roads.id
        )

        bikes.vertices.append(v2_bikes)
        bikes.vertices_by_id[v2_bikes.id] = v2_bikes
        bikes.nx_graph.add_node(v2_bikes.id)

    # dodajemy nowa krawedz
    bikes.nx_graph.add_edge(v1_bikes.id, v2_bikes.id)
    bikes.edges.append(
        Edge(
            id=len(bikes.edges)+1,
            v1=v1_bikes,
            v2=v2_bikes
        )
    )

    return bikes
