import sys
input = sys.stdin.readline

def b_search(arr, target):
    start = 0 
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
N_arr = list(map(int,input().split()))
M = int(input())
M_arr = list(map(int,input().split()))

N_arr.sort()

for target in M_arr:
    print(b_search(N_arr, target))
    
