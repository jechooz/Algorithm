def solution(slice, n):
    
    answer = 0
    return n//slice+1 if n % slice else n//slice