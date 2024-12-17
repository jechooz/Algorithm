import heapq as hq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
  
for _ in range(N):
    x = int(input())

    if x == 0:
        if len(heap) == 0:
              print(0)
        else:
             print(hq.heappop(heap))
    else:
        hq.heappush(heap, x)
    