from collections import deque

d = deque()

num = int(input())

for i in range(1, num+1):
    d.append(i)

while len(d) != 1:
    d.popleft()
    temp = d.popleft()
    d.append(temp)
print(d[0])
