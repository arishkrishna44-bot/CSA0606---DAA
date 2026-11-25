from itertools import permutations

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

min_cost = float("inf")
best_path = []

cities = list(range(1, n))

for path in permutations(cities):
    current_path = [0] + list(path) + [0]

    cost = 0

    for i in range(len(current_path) - 1):
        cost += graph[current_path[i]][current_path[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_path = current_path

print("Best path:", best_path)
print("Minimum cost:", min_cost)
