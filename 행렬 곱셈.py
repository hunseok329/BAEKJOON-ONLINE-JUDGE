a,b = map(int, input().split())

array1 = []

for _ in range(a):
    array1.append(list(map(int, input().split())))
    
c, d = map(int, input().split())

array2 = []

for _ in range(c):
    array2.append(list(map(int, input().split())))

for i in range(a):
    temp = ""
    for j in range(d):
        p = 0
        for w in range(c):
            p += array1[i][w] * array2[w][j]
        temp += str(p) + " "
    print(temp)