from pathlib import Path
from bike.util.parse import parse_qgis_data


def test_parse_qgis_data_bikes():

    vertices, edges = parse_qgis_data(
        Path('bike/test/qgis_data_test_bikes.csv'),
        delimiter=";"
    )

    assert len(vertices) == 22
    assert len(edges) == 21


def test_qgis_data_roads():

    vertices, edges = parse_qgis_data(
        Path('bike/test/qgis_data_test_roads.csv'),
        delimiter=";"
    )

    assert len(vertices) == 69
    assert len(edges) == 67
