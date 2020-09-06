a, b = map(int, input().split())

c = [True for x in range(b+1)]
c[0] = False
c[1] = False

for i in range(2, b+1):
    num = i*2
    while num <= b:
        c[num] = False
        num = num + i

for n in range(a, b+1):
    if c[n] == True:
        print(n)