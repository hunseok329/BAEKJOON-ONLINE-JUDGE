n = int(input())

arr = list(map(int, input().split()))

left = [1]*n
right = [1]*n

for x in range(1, n):

    for i in range(x):
        if arr[i] < arr[x] and left[i] >= left[x]:
            left[x] = left[i] + 1
    for i in range(1, x+1):
        if arr[-i] < arr[-(x+1)] and right[-i] >= right[-(x+1)]:
            right[-(x+1)] = right[-i] + 1

result = []

for x in range(n):
    result.append(left[x] + right[x])

print(max(result)-1)