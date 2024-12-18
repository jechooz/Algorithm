import sys
input = sys.stdin.readline
N,M = map(int,input().split())

set_n = set()
set_m = set()

for _ in range(N):
    set_n.add(input().strip())

for _ in range(M):
    set_m.add(input().strip())


result = sorted(set_n & set_m)

print(len(result))

for x in result:
    print(x)