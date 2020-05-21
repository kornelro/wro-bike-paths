from typing import Tuple, Dict
import numpy as np
import networkx as nx
from tqdm import tqdm


def _get_angle(p0: Tuple[float, float], p1: Tuple[float, float], p2=None):
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


def smooth_graph(
    G: nx.Graph,
    nodes: Dict(),
    angle_treshold: float = 90.
) -> nx.Graph:
    nodes_to_remove = []

    for node in tqdm(G.nodes):
        neighbors = G.neighbors(node)

        if len(neighbors) == 2:
            n1 = nodes.iloc[neighbors[0]]
            p1 = (n1['x'], n1['y'])

            n2 = nodes.iloc[node]
            p2 = (n2['x'], n2['y'])

            n3 = nodes.iloc[neighbors[1]]
            p3 = (n3['x'], n3['y'])

            angle = _get_angle(p1, p2, p3)
            if (angle > angle_treshold) and (360 - angle > angle_treshold):
                nodes_to_remove.append(node)

    for node in tqdm(nodes_to_remove):
        G.add_edge(*G.neighbors(node))
        G.remove_node(node)

    return G
