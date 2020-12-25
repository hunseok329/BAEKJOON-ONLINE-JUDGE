num = int(input())

arr = []

for _ in range(num):
    arr.append(int(input()))
    
dp = []

for i in range(num):
    if i == 0:
        dp.append(arr[i])
    elif i == 1:
        dp.append(max(dp[i-1] + arr[i], arr[i]))
    elif i < 3:
        dp.append(max(dp[i-2] + arr[i], arr[i-1] + arr[i]))
    else:
        dp.append(max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i]))
print(dp[-1])