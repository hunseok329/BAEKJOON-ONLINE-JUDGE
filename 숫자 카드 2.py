from sys import stdin

N = stdin.readline()
number = sorted(map(int, stdin.readline().split()))

M = stdin.readline()
checkNum = map(int, stdin.readline().split())

def search(n, p, front, end):
    if front > end:
        return 0
    half = (front+end)//2
    
    if n == p[half]:
        up, down = 1, 1
        while half + up <= end:
            if p[half] != p[half + up]:
                break
            else:
                up += 1
        while half - down >= front:
            if p[half] != p[half-down]:
                break
            else:
                down += 1
        return up + down - 1
    elif n < p[half]:
        return search(n, p, front, half-1)
    else:
        return search(n, p, half+1, end)
result = {}
for n in number:
    front = 0
    end = len(number)-1
    if n not in result:
        result[n] = search(n, number, front, end)
        
print(' '.join(str(result[x]) if x in result else '0' for x in checkNum ))