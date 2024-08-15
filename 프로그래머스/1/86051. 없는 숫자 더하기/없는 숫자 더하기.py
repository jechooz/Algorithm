def solution(numbers):
    
    arr = [ i for i in range(0,10)]
    
    for i in numbers:
        arr.remove(i)
        
    return sum(arr)