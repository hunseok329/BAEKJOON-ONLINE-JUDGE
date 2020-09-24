n,k = map(int, input().split())

numbers = []
count = 0

for _ in range(n):
    numbers.append(int(input()))
    
for i in range(n-1, -1, -1):
    if numbers[i] <= k:
        count += k//numbers[i]
        k = k%numbers[i]
print(count)