num = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(num):
    if numbers[i] == 1:
        continue
    elif numbers[i] == 2:
        count += 1
    else:
        for j in range(2, numbers[i]//2+1):
            if numbers[i] % j == 0:
                break
        else:
            count += 1
print(count)
