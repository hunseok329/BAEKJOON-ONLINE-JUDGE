import sys

num = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(num):
    order = str(sys.stdin.readline().rstrip())
    if order[:4] == "push":
        stack.append(int(order[5:]))
    elif order == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif order == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif order == "size":
        print(len(stack))
    else:
        if stack:
            print(stack.pop())
        else:
            print(-1)
