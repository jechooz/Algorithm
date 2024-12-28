import sys

t = int(sys.stdin.readline().strip())

s = [1, 1, 1]

for i in range(3, 100):
    s.append(s[i-2] + s[i-3])

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(s[n-1])

    