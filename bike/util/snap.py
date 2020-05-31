from bike.model.graph import Graph
from bike.model.vertex import Vertex
from bike.model.edge import Edge
import networkx as nx
from tqdm.auto import tqdm
import math


def __get_distance(v1: Vertex, v2: Vertex) -> float:
    distance = (v2.x - v1.x) ** 2 + (v2.y - v1.y) ** 2
    return math.sqrt(distance)


def __find_closest_vertex(base_vertex: Vertex, roads: Graph) -> Vertex:
    closest_vertex = None
    min_distance = float('inf')

    for vertex in roads.vertices:
        distance = __get_distance(base_vertex, vertex)

        if distance < min_distance:
            closest_vertex = vertex
            min_distance = distance

    return closest_vertex


def snap_vertices(roads: Graph, bikes: Graph) -> Graph:
    for vertex in tqdm(bikes.vertices, desc='Vertices'):
        closest_vertex = __find_closest_vertex(vertex, roads)

        # vertex.id = closest_vertex.id
        vertex.x = closest_vertex.x
        vertex.y = closest_vertex.y

    return bikes