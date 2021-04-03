from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    num_list = list(map(int, input().split()))
    if num_list[0] == 0 and len(num_list) == 1:
        break
    else:
        temp_list = list(combinations(num_list[1:], 6))
        for x in temp_list:
            for t in x:
                print(t, end=" ")
            print()
    print()