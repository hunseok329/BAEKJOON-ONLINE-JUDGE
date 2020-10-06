num = int(input())
numbers = list(map(int, input().split()))

dp = [0]*num

for i in range(num):
    dp[i] = 1
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))