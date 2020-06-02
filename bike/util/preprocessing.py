from typing import Tuple, List

import networkx as nx
import numpy as np
from tqdm.auto import tqdm

from bike.model.graph import Graph
from bike.model.edge import Edge


def smooth_graph(
    graph: Graph,
    angle_treshold: float = 135,
    snapped_ids: List[int] = []
) -> nx.Graph:
    nodes_to_remove = []
    G = graph.nx_graph

    for node in tqdm(G.nodes):
        neighbors = list(G.neighbors(node))

        if len(neighbors) == 2:
            n1 = graph.vertices_by_id[neighbors[0]]
            p1 = (n1.x, n1.y)

            n2 = graph.vertices_by_id[node]
            p2 = (n2.x, n2.y)

            n3 = graph.vertices_by_id[neighbors[1]]
            p3 = (n3.x, n3.y)

            angle = abs(_get_angle(p1, p2, p3))
            if (angle > angle_treshold) and (360 - angle > angle_treshold) and (n2.id not in snapped_ids):
                nodes_to_remove.append(node)

    for node in tqdm(nodes_to_remove):
        neighbors = list(G.neighbors(node))

        if len(neighbors) == 2:
            v1 = neighbors[0]
            v2 = neighbors[1]
            w1 = float(G.get_edge_data(v1, node)['weight'])
            w2 = float(G.get_edge_data(v2, node)['weight'])
            w = w1 + w2

        G.add_edge(v1, v2, weight=w)
        G.remove_node(node)

    graph.nx_graph = G

    return graph


def _get_angle(p0: Tuple[float, float], p1: Tuple[float, float], p2: Tuple[float, float]):
    ''' compute angle (in degrees) for p0p1p2 corner
    Inputs:
        p0,p1,p2 - points in the form of [x,y]
    '''
    if p2 is None:
        p2 = p1 + np.array([1, 0])
    v0 = np.array(p0) - np.array(p1)
    v1 = np.array(p2) - np.array(p1)

    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    return np.degrees(angle)


def remove_snapped(graph: Graph, snapped_ids: List[int]) -> Graph:
    for edge in tqdm(graph.nx_graph.edges):
        if edge[0] in snapped_ids and edge[1] in snapped_ids:
            graph.nx_graph.remove_edge(edge[0], edge[1])

    return graph


def update_edges(graph: Graph) -> Graph:

    current_edges = list(graph.nx_graph.edges)
    edges = []

    for i, edge in tqdm(enumerate(current_edges)):
        edges.append(
            Edge(
                id=i,
                v1=graph.vertices_by_id[edge[0]],
                v2=graph.vertices_by_id[edge[1]]
            )
        )

    graph.edges = edges

    return graph
