import sys
input = sys.stdin.readline


N = int(input())
times = list(map(int,input().split()))

times.sort()
sum = 0
now = 0

for i in times:
    now += i
    sum += now


print(sum)
    
