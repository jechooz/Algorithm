
import sys
from collections import deque

n,m = map(int,input().split())
graph = []
visited = [[0 for _ in range(m)] for i in range(n)]

for _ in range(n):
  graph.append(list(map(int,input().rstrip())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

  queue = deque()
  queue.append((x,y))
  visited[x][y] = 1

  while queue:
      x,y = queue.popleft()
  
      for i in range(4):
          nx = x+dx[i] 
          ny = y+dy[i]
          if nx<0 or ny<0 or nx>= n or ny>= m:
            continue
          if visited[nx][ny] == 0 and graph[nx][ny] == 1:
              visited[nx][ny] = visited[x][y] + 1  
              queue.append((nx,ny))
  return visited[n-1][m-1]
              

print(bfs(0,0))

        