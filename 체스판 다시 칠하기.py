N, M = map(int, input().split())

maps = []

for _ in range(N):
    maps.append(input())
    
def check(maps, x, y):
    cnt_b = 0
    cnt_w = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if 'B' != maps[y + i][x + j]:
                    cnt_b += 1
                else:
                    cnt_w += 1
            else:
                if 'B' != maps[y + i][x + j]:
                    cnt_w += 1
                else:
                    cnt_b += 1
    return cnt_b if cnt_b < cnt_w else cnt_w

result = float('inf')
for y in range(N-7):
    for x in range(M-7):
        temp = check(maps, x, y)
        result = temp if temp < result else result

print(result)


