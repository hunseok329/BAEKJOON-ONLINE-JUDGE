num = int(input())

p = []
rank = [1]*num

for _ in range(num):
    p.append(list(map(int, input().split())))

for i in range(num):
    for j in range(num):
        if j == i:
            continue
            
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            rank[i] += 1
for n in rank:
    print(n, end=" ")