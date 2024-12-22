import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[] for _ in range(n)]

visited = [False] * n
answer = False

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, depth):
    global answer
    if depth == 4:
        answer = True
        return
    
    visited[idx] = True
    for next_node in arr[idx]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)
            if answer:
                return
    visited[idx] = False

for i in range(n):
    dfs(i, 0)
    if answer:
        break

if answer:
    print(1)
else:
    print(0)
