import sys
input= sys.stdin.readline
from collections import deque
n,k = map(int,input().split())
queue = deque(range(1, n + 1))
answer = []


while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
        
print("<" + ", ".join(map(str, answer)) + ">")   