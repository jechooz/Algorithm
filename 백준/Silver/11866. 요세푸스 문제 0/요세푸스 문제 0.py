from collections import deque
import sys
input = sys.stdin.readline

def solution(N, K):
    q = deque(range(1, N + 1))
    result = []
    index = 0

    while q:
        index = (index + K - 1) % len(q)  
        result.append(q[index])
        q.remove(q[index])

    return result

N, K = map(int, input().split())
result = solution(N, K)
print("<" + ", ".join(map(str, result)) + ">")
