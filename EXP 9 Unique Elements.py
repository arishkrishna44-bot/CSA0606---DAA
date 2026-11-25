numbers = [1, 2, 3, 2, 4, 1, 5]

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Original list:", numbers)
print("Unique elements:", unique)

print("Space complexity: O(n)")
