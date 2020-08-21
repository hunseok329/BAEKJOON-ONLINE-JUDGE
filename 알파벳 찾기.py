word = input()
check = "abcdefghijklmnopqrstuvwxyz"
result = ""
for i in check:
    if i in word:
        c = word.find(i)
        result += str(c) + " "
    else:
        result += "-1 "
print(result)
