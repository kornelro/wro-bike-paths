# from evobench.benchmark import Benchmark
# from evobench.model import Population
# from pytest import fixture

# from ..translation import Translation


# @fixture
# def translation(benchmark: Benchmark) -> Translation:
#     return Translation(
#         benchmark,
#         prob=0.5,
#         factor=0.1,
#         gene_prob=0.1
#     )


# def test_translation(translation: Translation, population: Population):
#     new_population = translation(population)

#     assert len(population.solutions) < len(new_population.solutions)
