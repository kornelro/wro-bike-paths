from pathlib import Path
from bike.util.parse import parse_qgis_data


def test_parse_qgis_data():

    vertices, edges = parse_qgis_data(
        Path('bike/test/qgis_data_test.csv'),
        delimiter=";",
        save_to_files=False,
        output=Path('../data/')
    )

    assert len(vertices) == 13
    assert len(edges) == 10
