import sys

N, C = map(int, sys.stdin.readline().split())

home = [int(sys.stdin.readline()) for _ in range(N)]

home.sort()
start, end = 1, home[-1]-home[0]

def home_count(dis):
    std = home[0]
    count = 1
    for i in range(1, len(home)):
        if dis + std <= home[i]:
            count += 1
            std = home[i]
    return count

while start <= end:
    mid = (start+end)//2

    if home_count(mid) >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)