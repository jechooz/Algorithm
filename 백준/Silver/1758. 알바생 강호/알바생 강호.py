import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)
result = 0
for rank, x in enumerate(arr):
    if x - rank <= 0:
        break
    result += x - rank
print(result)