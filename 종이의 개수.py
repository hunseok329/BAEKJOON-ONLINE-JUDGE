num = int(input())

maps = []

result = [0,0,0]

for _ in range(num):
    maps.append(list(map(int, input().split())))
    
def cut(x, y, n):
    global result    
    div = n//3
    if cut_check(x, y, n):
        result[maps[y][x] + 1] += 1
    else:
        cut(x, y, div)
        cut(x + div, y, div)
        cut(x + div*2, y, div)
        cut(x, y + div, div)
        cut(x + div, y + div, div)
        cut(x + div*2, y + div, div)
        cut(x, y + div*2, div)
        cut(x + div, y + div*2, div)
        cut(x + div*2, y + div*2, div)
    
def cut_check(x, y, n):
    temp = maps[y][x]
    
    for i in range(n):
        for j in range(n):
            if temp != maps[y+i][x+j]:
                return False
    return True

cut(0, 0, num)
            
print(maps)
print(result[0])
print(result[1])
print(result[2])