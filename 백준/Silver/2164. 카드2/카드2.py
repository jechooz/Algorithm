from collections import deque

d = deque()

N = int(input())
for i in range(1,N+1):
    d.append(i)

while d:
    if len(d) == 1:
        print(d.pop())
        break
  
    d.popleft()
    card = d.popleft()
    d.append(card)
  