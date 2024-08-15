def solution(arr):
    newarr=sorted(arr)
    arr.remove(newarr[0])
    
    if len(arr)<=1:
        arr.append(-1)
    
    return arr