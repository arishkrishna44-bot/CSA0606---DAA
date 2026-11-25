n = int(input("Enter number of dice: "))
m = int(input("Enter number of faces: "))
target = int(input("Enter target sum: "))

dp = [[0] * (target + 1) for _ in range(n + 1)]

dp[0][0] = 1

for dice in range(1, n + 1):
    for total in range(1, target + 1):
        for face in range(1, m + 1):
            if total >= face:
                dp[dice][total] += dp[dice - 1][total - face]

print("Number of ways:", dp[n][target])
