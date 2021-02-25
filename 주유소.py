l = int(input())

road = list(map(int, input().split()))
oil = list(map(int, input().split()))

now = oil[0]
total = 0
for x in range(len(oil)-1):
    if now > oil[x]:
        now = oil[x]
    total += now * road[x]
print(total)