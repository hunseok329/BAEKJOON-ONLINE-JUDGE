while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0 and numbers[1] == 0:
        break
    if numbers[0] > numbers[1]:
        p = numbers[0] % numbers[1]
        if p != 0:
            print("neither")
        else:
            print("multiple")
    else:
        p = numbers[1] % numbers[0]
        if p != 0:
            print("neither")
        else:
            print("factor")