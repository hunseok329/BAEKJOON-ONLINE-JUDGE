num = int(input())

pado = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90

for i in range(11, 101):
    pado[i] = pado[i-1] + pado[i-5]

for _ in range(num):
    print(pado[int(input())])