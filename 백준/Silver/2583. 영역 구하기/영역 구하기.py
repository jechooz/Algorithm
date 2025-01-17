from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(list(map(int, input().split())))

graph = [[0] * m for _ in range(n)]

# 벽을 표시
for a in arr:
    start_x, start_y, end_x, end_y = a
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            graph[x][y] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    result = 1
    q = deque()
    q.append((x, y))
    graph[x][y] = 1  
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1  
                result += 1
                q.append((nx, ny))
    return result

result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:  
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)




  

      