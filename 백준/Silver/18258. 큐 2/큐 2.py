import sys
input = sys.stdin.readline

from collections import deque
q = deque()


N = int(input())
for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        print(-1) if len(q) == 0 else print(q.popleft())
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        print(1) if len(q) == 0 else print(0)
    elif order[0] == 'front':
        print(-1) if len(q) == 0 else print(q[0])
    elif order[0] == 'back':
        print(-1) if len(q) == 0 else print(q[-1])