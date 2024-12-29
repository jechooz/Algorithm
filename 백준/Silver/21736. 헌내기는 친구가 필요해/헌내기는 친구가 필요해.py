import sys
input = sys.stdin.readline
from collections import deque

#설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]
campus = []
ix, iy = 0,0
person = 0

#입력
N,M = map(int,input().split())
for i in range(N):
    campus.append(list(input()))
    for j in range(M):
        #시작위치
        if campus[i][j] == 'I':
            ix, iy = i,j

visited = [[0]* M for _ in range(N)]
q = deque()
q.append([ix,iy])


while q:
    x,y = q.popleft();
    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if 0<= nx < N and 0<= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if campus[nx][ny] == 'O':
                    q.append([nx,ny])
                if campus[nx][ny]=='P':
                    q.append([nx,ny])
                    person += 1

if person == 0:
    print('TT')
else:
    print(person)