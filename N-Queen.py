n = int(input())

col = [True] * n
up = [True] * (2*n-1)
down = [True] * (2*n-1)

count = 0

def Nqueen(index, n):
    global count
    if index == n:
        count += 1
        return

    for i in range(n):
        if (col[i] and up[index + i] and down[index-i+n-1]):
            col[i] = up[index + i] = down[index-i+n-1] = False
            Nqueen(index + 1, n)
            col[i] = up[index + i] = down[index-i+n-1] = True
            
Nqueen(0, n)
print(count)