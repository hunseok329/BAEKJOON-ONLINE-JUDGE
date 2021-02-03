num = int(input())

arr = []
dp = [1] * num

for _ in range(num):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x : x[0])

for i in range(num):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(num-max(dp))