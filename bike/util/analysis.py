import matplotlib.pyplot as plt
import time
import multiprocessing.pool
import functools
import numpy as np
from IPython.display import display
from networkx.algorithms.distance_measures import diameter
from networkx import degree, betweenness_centrality, closeness_centrality, degree_histogram
from networkx.algorithms.link_analysis.pagerank_alg import pagerank
from networkx.algorithms.components import connected_components
from networkx.classes.function import density
from networkx.algorithms.cluster import clustering
from networkx.algorithms.approximation.clustering_coefficient import average_clustering
from networkx.algorithms.shortest_paths.generic import average_shortest_path_length


TIMEOUT = 30


def timeout(max_timeout):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            pool = multiprocessing.pool.ThreadPool(processes=1)
            async_result = pool.apply_async(item, args, kwargs)
            # raises a TimeoutError if execution exceeds max_timeout
            return async_result.get(max_timeout)
        return func_wrapper
    return timeout_decorator


@timeout(TIMEOUT)
def run(G, method, method_name):
    t = -1
    try:
        start = time.time()
        res = method(G)
        end = time.time()
        t = end-start
    except Exception as e:
        print('Błąd podczas liczenia '+method_name+': ', e)
        print()
    return [res, t]


def run_with_timeout(G, method, method_name):
    res = [0, -1]
    try:
        res = run(G, method, method_name)
    except Exception as e:
        print('Błąd podczas liczenia '+method_name+': ', e)
        print()
    return res


def print_results(method_name, results):
    print('### '+method_name+' ###')
    print('Wynik :', results[0])
    print('Czas obliczeń :', results[1])
    print()


def run_analysis(G, vis=False):

    # degree
    res = run_with_timeout(G, degree, 'degree median')
    if res[1] >= 0:
        res[0] = np.median(np.array(list(map(lambda x: x[1], list(res[0])))))
        print_results('degree median', res)

    # betweenness_centrality
    res = run_with_timeout(G, betweenness_centrality, 'betweenness centrality median')
    if res[1] >= 0:
        res[0] = np.median(np.array(list(res[0].values())))
        print_results('betweenness centrality median', res)

    # closeness_centrality
    res = run_with_timeout(G, closeness_centrality, 'closeness centrality median')
    if res[1] >= 0:
        res[0] = np.median(np.array(list(res[0].values())))
        print_results('closeness centrality median', res)

    # clustering coefficient
    res = run_with_timeout(G, average_clustering, 'clustering coefficient')
    if res[1] >= 0:
        print_results('clustering coefficient', res)

    # average shortest path length
    res = run_with_timeout(G, average_shortest_path_length, 'shortest path mean')
    if res[1] >= 0:
        print_results('shortest path mean', res)

    # pagerank
    res = run_with_timeout(G, pagerank, 'pagerank median')
    if res[1] >= 0:
        res[0] = np.median(np.array(list(res[0].values())))
        print_results('pagerank median', res)

    # diameter
    res = run_with_timeout(G, diameter, 'diameter')
    if res[1] >= 0:
    # res[0] = np.mean(np.array(list(res[0].values())))
        print_results('diameter', res)

    # connected_components
    res = run_with_timeout(G, connected_components, 'number of connected components')
    if res[1] >= 0:
        res[0] = len([x for x in res[0]])
        print_results('number of connected components', res)

    # density
    res = run_with_timeout(G, density, 'density')
    if res[1] >= 0:
        print_results('density', res)

    if vis:

        # degree distribution
        res = run_with_timeout(G, degree_histogram, 'degree histogram')
        if res[1] >= 0:
            plt.bar(range(len(res[0])), res[0])
            plt.title('DEGREE DISTRIBUTION')
            display(plt.show())
            print('Czas: ', res[1])
            print()

        # clustering coefficient distribution
        res = run_with_timeout(G, clustering, 'clustering coefficient')
        if res[1] >= 0:
            plt.hist(list(res[0].values()))
            plt.title('CLUSTERING COEFFICIENT DISTRIBUTION')
            display(plt.show())
            print('Czas: ', res[1])
            print()
