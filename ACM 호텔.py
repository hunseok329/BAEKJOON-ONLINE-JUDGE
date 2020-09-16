num = int(input())

for _ in range(num):
    H,W,N = map(int, input().split())
    
    floor = N%H
    div = N//H
    if floor != 0:
        div += 1
    else:
        floor = str(H)
    
    if div < 10:
        div = "0" + str(div)
    print(str(floor) + str(div))