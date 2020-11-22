num = int(input())

maps = []

blue = 0
white = 0

for _ in range(num):
    maps.append(list(map(int, input().split())))
    
def ch(x, y, n):
    if n == 0:
        return 0
    global blue
    global white
    half = n//2
    p = 0
    
    for i in range(n):
        p += sum(maps[y+i][x:x+n])
    
    if p == 0:
        white += 1
        return 0
    elif p == n*n:
        blue += 1
        return 0
    else:
        return ch(x, y, half) + ch(x+half, y, half) + ch(x, y+half, half) + ch(x+half, y+half, half)
    
ch(0,0,num)

print(white)
print(blue)