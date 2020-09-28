check = ['[', '(', ')', ']']

while True:
    string = str(input())
    stack = []
    if string == '.':
        break
    for i in string:
        if i in check:
            if stack:
                if stack[-1] == '[' and i == ']':
                    stack.pop()
                elif stack[-1] == '(' and i == ')':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    if stack:
        print('no')
    else:
        print('yes')
