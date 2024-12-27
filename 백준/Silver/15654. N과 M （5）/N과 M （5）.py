import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

result = []
visited = [False] * n

def dfs(depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if visited[i]: continue
        visited[i] = True
        result.append(arr[i])
        dfs(depth + 1)
        result.pop()
        visited[i] = False

dfs(0)
