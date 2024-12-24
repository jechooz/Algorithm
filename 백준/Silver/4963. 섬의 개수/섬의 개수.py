import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0 

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                queue.append((nx, ny))
                graph[ny][nx] = 0  

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0  
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                BFS(j, i)
                cnt += 1
    print(cnt)

