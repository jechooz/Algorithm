X=int(input())
N=int(input())
sum = 0

for i in range(N):
    PRICE,COUNT = map(int,input().split())
    sum+=PRICE*COUNT
    
if sum == X:
    print('Yes')
else:
    print('No')