nums = [1, 2, 1, 2, 1]
k = 2

count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1

print("Number of pairs:", count)
