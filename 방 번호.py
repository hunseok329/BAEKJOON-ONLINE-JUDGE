num = str(input())

pack = [0] * 11

for w in num:
    if pack[int(w)] == 0:
        if w == '6' and pack[9] != 0:
            pack[9] -= 1
        elif w == '9' and pack[6] != 0:
            pack[6] -= 1
        else:
            for x in range(11):
                pack[x] += 1
            pack[int(w)] -= 1
    else:
        pack[int(w)] -= 1
print(pack[-1])