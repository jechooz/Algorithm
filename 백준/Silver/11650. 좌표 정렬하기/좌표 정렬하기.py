import sys
input = sys.stdin.readline

N = int(input())
arr = []

#입력
for i in range(N):
    a, b = map(int,input().split())
    arr.append((a,b))
         
arr.sort()

#출력
for x in arr:
    print(x[0], x[1] )
    



