num = int(input())

stack = []

for _ in range(num):
    number = int(input())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()
print(sum(stack))
