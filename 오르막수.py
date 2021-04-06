num = int(input())

dp = [[1 for _ in range(10)] for _ in range(num+1)]

for y in range(2, num+1):
    for x in range(1, 10):
        dp[y][x] = dp[y-1][x] + dp[y][x-1]

print(sum(dp[num])%10007)