# Traveling Salesman Problem using Nearest Neighbor Heuristic


This Python script provides a simple implementation for 
solving the`TSP` using the `Nearest Neighbor algorithm`. The TSP is a classic optimization problem where the goal is to find the shortest possible tour that visits a set of cities and returns to the starting city.




# Code Overview

## Euclidian distance function

This function calculates the `Euclidean distance` between two cities based on their coordinates, using this formula: 

d ( x , y ) = $\sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}$


- It first checks if the cities have the same dimension (i.e., the same number of coordinates).

- It then computes the squared distance for each dimension, sums them up, and takes the square root to obtain the final Euclidean distance.



## Nearest Neighbor 

- It starts from a specified city (start_city) and iteratively selects the nearest unvisited city to extend the path.
- The algorithm iterate over all the cities and always take the nearest city by using the euclidian distance function and save the path in a list .
- The result is a list representing the optimal path that visits all cities based on the Nearest Neighbor heuristic.