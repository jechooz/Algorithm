import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())
day = 0

day = (v-b)/(a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day)+1)
    
