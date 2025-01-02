import sys
input = sys.stdin.readline

#가지고 있는 카드 n개
n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()

#구해야할 카드 m개
m = int(input())
arr2 = list(map(int,input().split()))

#이진탐색
def bsearch(arr,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bsearch(arr,target,start,mid-1)
    elif arr[mid] < target:
        return bsearch(arr,target,mid+1,end)


card_count = {}
for _ in arr1:
    if _ not in card_count:
        card_count[_] = 1
    else:
        card_count[_] +=1


for i in arr2:    
    result = bsearch(arr1,i,0,n-1)
    if result is not None:
        print(card_count[i],end=' ')
    else:
        print(0, end = ' ')
  
