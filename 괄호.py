num = int(input())

for _ in range(num):
    count = []
    s = str(input())
    for i in s:
        if count:
            if count[-1] == '(' and i == ')':
                count.pop()
            else:
                count.append(i)
        else:
            count.append(i)
    if count:
        print('NO')
    else:
        print('YES')
