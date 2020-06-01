from pytest import fixture
from bike.model.graph import Graph
from pathlib import Path


VERTICES_BIKES_PATH = Path('bike/test/vertices_test_bikes.csv')
EDGES_BIKES_PATH = Path('bike/test/edges_test_bikes.csv')

VERTICES_ROADS_PATH = Path('bike/test/vertices_test_roads.csv')
EDGES_ROADS_PATH = Path('bike/test/edges_test_roads.csv')


@fixture(scope='session')
def graph_bikes() -> Graph:
    return Graph(VERTICES_BIKES_PATH, EDGES_BIKES_PATH)


@fixture(scope='session')
def graph_roads() -> Graph:
    return Graph(VERTICES_ROADS_PATH, EDGES_ROADS_PATH)
