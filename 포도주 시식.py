n = int(input())

arr = [0]

for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n+1)

for x in range(1, n+1):
    if x < 3:
        dp[x] = dp[x-1] + arr[x]
    else:
        dp[x] = max(dp[x-3] + arr[x-1] + arr[x], dp[x-2] + arr[x], dp[x-1])
print(dp[-1])