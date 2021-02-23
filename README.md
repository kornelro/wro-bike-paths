wro-bike-paths
================

This project implements idea to optimize building new bike paths using genetic algorithm and considering existing paths network as a graph. In this approach choosen optimization method looks for new edges in graph that minimize one of three criterion:
- **average betweenness centrality** - we want to minimize situation that few paths are much more crowded than others, so our goal is to get more equal usage of all paths,
- **average shortest path** - it’s natural that we want to move around the city faster,
- **clustering coefficient** - more clustered paths mean that we can efficiently move around one place but we prefer to build new paths where there is lack of infrastructure.

Presented proof of concept was built upon Wroclaw city infrastructure data from OpenStreetMap.

Check [the project poster](https://github.com/piotr-rarus/wro-bike-paths/blob/master/assets/poster.pdf) to see more details.