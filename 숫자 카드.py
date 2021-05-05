import sys

input = sys.stdin.readline

N = int(input())

N_list = set(map(int, input().split()))

M = int(input())

M_list = list(map(int, input().split()))

result = ""

for x in M_list:
    if x in N_list:
        result += "1 "
    else:
        result += "0 "

print(result)