while True:
    p = list(map(int, input().split()))
    p = sorted(p)
    if sum(p) == 0:
        break
    if p[2]**2 == p[1]**2 + p[0]**2:
        print('right')
    else:
        print('wrong')