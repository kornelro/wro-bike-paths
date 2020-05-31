from pathlib import Path

import pandas as pd
from tqdm.auto import tqdm


def get_vertices_id(
    x: float,
    y: float,
    vertices: pd.DataFrame
) -> int:
    return vertices[vertices['x'] == x][vertices['y'] == y].index[0]


def parse_qgis_data(
    path: Path,
    delimiter: str = ';'
) -> (pd.DataFrame, pd.DataFrame):

    data = pd.read_csv(path, delimiter=delimiter)
    data = data[data['xcoord'] != 0]

    vertices = data[['xcoord', 'ycoord']]
    vertices = vertices.drop_duplicates().reset_index(drop=True)
    vertices = vertices.rename(columns={'ycoord': 'y', 'xcoord': 'x'})

    edges = pd.DataFrame(columns=['v1', 'v2'])

    for i in tqdm(range(1, len(data))):

        if int(data.iloc[i]['vertex_index']) > 0:
            try:
                r1 = data.iloc[i-1]
                r2 = data.iloc[i]
                row = {
                    'v1': get_vertices_id(
                        r1['xcoord'],
                        r1['ycoord'],
                        vertices
                    ),
                    'v2': get_vertices_id(
                        r2['xcoord'],
                        r2['ycoord'],
                        vertices
                    )
                }
                edges = edges.append(row, ignore_index=True)
            except Exception:
                print('Cannot parse rows: ', i-1, ', ', i)

    return vertices, edges
