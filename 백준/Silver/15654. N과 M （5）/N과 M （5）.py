import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for p in permutations(arr, m):
    print(*p)
