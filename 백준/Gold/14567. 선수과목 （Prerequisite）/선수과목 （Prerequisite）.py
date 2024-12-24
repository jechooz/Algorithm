import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
semester =  [1] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    current = q.popleft()
    
    for next in graph[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
        
        semester[next] = max(semester[next], semester[current] + 1)

print(*semester[1:])