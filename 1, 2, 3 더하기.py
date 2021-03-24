t = int(input())

num = []

for _ in range(t):
    num.append(int(input()))
    
for i in num:
    dp = [1] * (i+1)
    for x in range(1, i+1):
        if x == 1:
            dp[x] = 1
        elif x == 2:
            dp[x] = 2
        else:
            dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
    print(dp[-1])