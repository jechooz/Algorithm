import sys
input = sys.stdin.readline

N,M = map(int,input().split())
result = []


def solution(level,start):
    if level == M:
        print(' '.join(map(str,result)))
        return
    for i in range(start,N+1):
            result.append(i)
            solution(level+1,i+1)
            result.pop()
            

solution(0, 1)