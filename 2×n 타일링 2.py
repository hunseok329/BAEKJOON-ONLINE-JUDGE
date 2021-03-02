n = int(input())

dp = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    dp[1] = 1
    dp[2] = 3
    for x in range(3, n+1):
        dp[x] = (dp[x-1] + ((dp[x-2]) * 2)) % 10007
    print(dp[-1])