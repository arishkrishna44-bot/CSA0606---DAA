import math

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10)]

min_distance = float("inf")
closest_pair = None

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        if distance < min_distance:
            min_distance = distance
            closest_pair = (points[i], points[j])

print("Closest pair:", closest_pair)
print("Minimum distance:", round(min_distance, 2))
