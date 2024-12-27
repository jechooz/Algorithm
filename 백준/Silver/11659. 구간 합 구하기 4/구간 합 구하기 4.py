import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

psum = [0]
total = 0
for i in range(len(arr)):
    total += arr[i]
    psum.append(total)

for _ in range(m):
    i, j = map(int, input().split())
    print(psum[j] - psum[i - 1])
