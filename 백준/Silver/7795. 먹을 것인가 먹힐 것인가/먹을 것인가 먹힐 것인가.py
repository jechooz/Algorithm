import sys
input = sys.stdin.readline

def b_search(arr, target):
    left,right = 0,len(arr)
    while left<right:
        mid = (left+right)//2
        if arr[mid] <target:
            left = mid+1
        else:
            right = mid
            
    return left    
    
def solution(a_size,b_size):    

    b_size.sort()
    count = 0

    for a in a_size:
        count += b_search(b_size,a)
    return count


T = int(input())

for _ in range(T):
    N,M = map(int,input().split())

    a_size = list(map(int,input().split()))
    b_size = list(map(int,input().split()))
    
    print(solution(a_size,b_size))



                