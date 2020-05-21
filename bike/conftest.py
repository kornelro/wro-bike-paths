from pytest import fixture
from bike.model.graph import Graph
from pathlib import Path


VERTICES_PATH = Path('bike/test/vertices.csv')
EDGES_PATH = Path('bike/test/edges.csv')


@fixture(scope='session')
def graph() -> Graph:
    return Graph(VERTICES_PATH, EDGES_PATH)
