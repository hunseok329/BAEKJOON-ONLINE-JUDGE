import math

num = int(input())


for _ in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    if distance == 0 and r1 == r2:
        print(-1)
    elif r1+r2 > distance:
        if abs(r1-r2) > distance:
            print(0)
        elif abs(r1-r2) == distance:
            print(1)
        else:
            print(2)
    elif r1+r2 == distance:
        print(1)
    else:
        print(0)