num = int(input())
names = []
for _ in range(num):
    names.append(list(map(str, input().split())))
names = sorted(names, key = lambda x : int(x[0]))
for year, name in names:
    print(year + " " + name)