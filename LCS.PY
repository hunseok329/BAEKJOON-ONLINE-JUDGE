f = ' ' + input()
e = ' ' + input()

dp = [[0] * len(f) for _ in range(len(e))]

for y in range(1, len(e)):
    for x in range(1, len(f)):
        if f[x] == e[y]:
            dp[y][x] = dp[y-1][x-1] + 1
        else:
            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
print(dp[-1][-1])