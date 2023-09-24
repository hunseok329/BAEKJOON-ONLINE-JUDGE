K, N = map(int, input().split())

line = []

for _ in range(K):
    line.append(int(input()))

start, end = 1, max(line)

while start <= end:
    mid = (start+end)//2
    
    count = 0
    for x in line:
        count += x//mid
        
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)


k, n = list(map(int, input().split()))

lines = [int(input()) for _ in range(k)]

start, end = 0, max(lines)

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for line in lines:
        cnt += line//mid
        
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)