import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) < 2:
        return arr 
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    result_arr = [] 
    
    l = 0
    r = 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            result_arr.append(left_arr[l])
            l += 1
        else:
            result_arr.append(right_arr[r])
            r += 1
    result_arr += left_arr[l:]
    result_arr += right_arr[r:]
    return result_arr
    
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
result_arr = merge_sort(arr) 
    
for i in result_arr:
    print(i)
