from lazy_property import LazyProperty, LazyWritableProperty
from pathlib import Path
from bike.model.edge import Edge
from bike.model.vertex import Vertex
from typing import List, Dict
import pandas as pd
import networkx as nx


class Graph:

    def __init__(self, vertices_path: Path, edges_path: Path):
        self.VERTICES_PATH = vertices_path
        self.EDGES_PATH = edges_path

    @LazyWritableProperty
    def vertices(self) -> List[Vertex]:
        vertices = []
        vertices_pd = pd.read_csv(self.VERTICES_PATH)

        for index, row in vertices_pd.iterrows():
            vertex = Vertex(
                id=row['id'],
                x=row['x'],
                y=row['y']
            )

            vertices.append(vertex)

        return vertices

    @LazyProperty
    def vertices_by_id(self) -> Dict[int, Vertex]:
        vertices_by_id = {}

        for vertex in self.vertices:
            vertices_by_id[vertex.id] = vertex

        return vertices_by_id

    @LazyWritableProperty
    def edges(self) -> List[Edge]:
        edges = []
        edges_pd = pd.read_csv(self.EDGES_PATH)
        edges_pd.fillna(0)

        for index, row in edges_pd.iterrows():
            edge = Edge(
                id=row['id'],
                v1=self.vertices_by_id[row['v1']],
                v2=self.vertices_by_id[row['v2']],
            )

            edges.append(edge)

        return edges

    @LazyProperty
    def nx_graph(self) -> nx.Graph:
        graph = nx.Graph()
        for edge in self.edges:
            graph.add_edge(
                edge.v1.id,
                edge.v2.id,
                weight=edge.distance
            )

        return graph
