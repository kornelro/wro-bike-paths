import pandas as pd
from tqdm import tqdm


def get_vertice_id(
    x: float,
    y: float,
    vertices: pd.DataFrame
) -> int:
    return vertices[vertices['x'] == x][vertices['y'] == y].index[0]


def parse_qgis_data(
    path: str,
    delimiter: str = ';',
    save_to_files: bool = False,
    save_path: str = './'
) -> (pd.DataFrame, pd.DataFrame):

    data = pd.read_csv(path, delimiter=delimiter)
    data = data[data['xcoord'] != 0]

    vertices = data[['xcoord', 'ycoord']]
    vertices = vertices.drop_duplicates().reset_index(drop=True)
    vertices = vertices.rename(columns={'ycoord': 'y', 'xcoord': 'x'})

    edges = pd.DataFrame(columns=['v1', 'v2', 'type', 'direction', 'distance'])
    for i in tqdm(range(0, len(data), 2)):
        try:
            r1 = data.iloc[i]
            r2 = data.iloc[i+1]
            row = {
                'v1': get_vertice_id(r1['xcoord'], r1['ycoord'], vertices),
                'v2': get_vertice_id(r2['xcoord'], r2['ycoord'], vertices),
                'type': r1['TYP'],
                'direction': r1['KIERUNEK'],
                'distance': r1['SHAPE_LEN']
            }
            edges = edges.append(row, ignore_index=True)
        except:
            print('Cannot parse rows: ', i, ', ', i+1)

    if save_to_files:
        edges.to_csv(save_path+'edges.csv', index_label='id')
        vertices.to_csv(save_path+'vertices.csv', index_label='id')

    return vertices, edges
