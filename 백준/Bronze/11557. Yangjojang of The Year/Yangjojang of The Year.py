import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dict = {}
    for _ in range(n):
        school, alch = input().split()
        dict[school] = int(alch)
    max_school = max(dict,key = dict.get)
    print(max_school)