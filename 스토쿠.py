import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def row(y, i):
    if i in sudoku[y]:
        return False
    return True

def col(x, i):
    for z in range(9):
        if i == sudoku[z][x]:
            return False
    return True

def box(x, y, v):
    dx = x//3 * 3
    dy = y//3 * 3
    for i in range(3):
        for j in range(3):
            if v == sudoku[dy+i][dx+j]:
                return False
    return True

def sdk(index):
    if index == len(zeros):
        for re in sudoku:
            for n in re:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:  
        y = zeros[index][0]
        x = zeros[index][1]
    
        for i in range(1, 10):
            if row(y, i) and col(x, i) and box(x, y, i):
                sudoku[y][x] = i
                sdk(index+1)
                sudoku[y][x] = 0

sdk(0)