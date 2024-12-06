import sys
sys.setrecursionlimit(200000)

def dfs(node):
    for neighbor in graph[node]:
        if parent[neighbor] == -1:
            parent[neighbor] = node
            dfs(neighbor)

input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent[1] = 0
dfs(1)

for i in range(2, N+1):
    print(parent[i])
