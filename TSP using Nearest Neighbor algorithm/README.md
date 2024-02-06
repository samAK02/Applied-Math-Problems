# Traveling Salesman Problem using Nearest Neighbor Heuristic


This Python script provides a simple implementation for 
solving the`TSP` using the `Nearest Neighbor algorithm`. The TSP is a classic optimization problem where the goal is to find the shortest possible tour that visits a set of cities and returns to the starting city.




# Code Overview

## Euclidean distance function

This function calculates the `Euclidean distance` between two cities based on their coordinates, using this formula: 

d ( x , y ) = $\sqrt{\sum_{i=1 } ^ { n}   (x_i - y_i)^2}$


- It first checks if the cities have the same dimension (i.e., the same number of coordinates).

- It then computes the squared distance for each dimension, sums them up, and takes the square root to obtain the final Euclidean distance.



## Nearest Neighbor 

- It starts from a specified city (start_city) and iteratively selects the nearest unvisited city to extend the path.
- The algorithm iterates over all the cities and always take the nearest city by using the euclidean distance function and save the path in a list .
- The result is a list representing the optimal path that visits all cities based on the Nearest Neighbor heuristic.


## Example of Use

Let's take those cities with their coordinates:

    cities = [
    {'name': 'Strasbourg', 'coordinates': ('48.5734', '7.7521')},
    {'name': 'Paris', 'coordinates': ('48.8566', '2.3522')},
    {'name': 'Grenoble', 'coordinates': ('45.1885', '5.7245')},
    {'name': 'Toulouse', 'coordinates': ('43.6047', '1.4442')}
    ]   

The output will be: 

