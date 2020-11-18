N, M = map(int, input().split())

n = list(map(int, input().split()))
num = [x for x in range(1, N+1)]
index = 0
count = 0

for i in n:
    find = num.index(i)
    up = 0
    down = 0
    if find > index:
        up = find - index
        down = len(num) - find + index
    elif find < index:
        up = len(num) - index + find
        down = index - find
        
    if up >= down:
        count += down
    else:
        count += up

    index = find
    num.pop(find)
print(count)