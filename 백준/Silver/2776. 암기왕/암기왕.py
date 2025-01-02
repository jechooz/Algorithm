import sys
input = sys.stdin.readline



def bsearch(arr,target,start,end):
    if start > end:
        return False
    mid = (start+end)//2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return bsearch(arr,target,start,mid-1)
    elif arr[mid] < target:
        return bsearch(arr,target,mid+1,end)
        
T = int(input()) 

for _ in range(T):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr1.sort()
    
    m = int(input())
    arr2 = list(map(int,input().split()))
            
    for i in arr2:
        if bsearch(arr1,i,0,n-1):
            print(1)
        else:
            print(0)