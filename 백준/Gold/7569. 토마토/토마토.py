import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [[[0] * M for _ in range(N)] for _ in range(H)]
q = deque()

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            arr[i][j][k] = row[k]
            if arr[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and arr[nx][ny][nz] == 0:
                arr[nx][ny][nz] = arr[x][y][z] + 1
                q.append((nx, ny, nz))

bfs()

tomato = False
answer = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                tomato = True
            answer = max(answer, arr[i][j][k])

if tomato:
    answer = -1
elif answer == 1:
    answer = 0
else:
    answer -= 1

print(answer)
