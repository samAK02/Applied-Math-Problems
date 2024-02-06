import math

def euclid_dist(city1, city2):
    if len(city1['coordinates']) != len(city2['coordinates']):
        raise ValueError("the nodes don't have the same dimension")


    squared_dist = sum((float(x) - float(y)) ** 2 for x, y in zip(city1['coordinates'], city2['coordinates']))
    return math.sqrt(squared_dist)

def nearest_neighbor(cities, start_city):
    start_city = 0
    n = len(cities)
    visited = [False] * n
    path = [start_city]
    visited[start_city] = True

    for _ in range(n - 1):
        current_city = path[-1]
        nearest_city = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i]:
                d = euclid_dist(cities[current_city], cities[i])
                if d < min_dist:
                    min_dist = d
                    nearest_city = i

        path.append(nearest_city)
        visited[nearest_city] = True

    return path

# Example of use with cities and their coordinates
cities = [
    {'name': 'Strasbourg', 'coordinates': ('48.5734', '7.7521')},
    {'name': 'Paris', 'coordinates': ('48.8566', '2.3522')},
    {'name': 'Grenoble', 'coordinates': ('45.1885', '5.7245')},
    {'name': 'Toulouse', 'coordinates': ('43.6047', '1.4442')}
]

# Specify the starting city index (Strasbourg in this case)
starting_city_index = 0


optimal_path = nearest_neighbor(cities, start_city= starting_city_index)


optimal_path_names = []
for i in optimal_path:
    optimal_path_names.append(cities[i]['name'])
print("Optimal path starting from Strasbourg:", optimal_path_names)
