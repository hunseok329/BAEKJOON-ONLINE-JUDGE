n = int(input())

arr_a = list(map(int, input().split()))

arr_b = list(map(int, input().split()))

arr_a.sort()
arr_b.sort(reverse=True)

result = 0

for x in range(n):
    result += arr_a[x] * arr_b[x]

print(result)