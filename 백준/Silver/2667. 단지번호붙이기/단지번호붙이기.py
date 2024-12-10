from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    count = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and not visited[x][y]:
            count = bfs(x, y)
            answer.append(count)

print(len(answer))
for count in sorted(answer):
    print(count)