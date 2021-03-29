import sys

input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(list(map(int, input().split())))

dp = [0] * (n+1)

for i in range(n):
    index, cost = numbers[i][0], numbers[i][1]
    if i > 0:
        if dp[i-1] > dp[i]:
            dp[i] = dp[i-1]
    if i+index <= n and dp[i+index] < dp[i] + cost:
        dp[i+index] = dp[i] + cost
print(max(dp))