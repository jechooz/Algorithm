def solution(a, b):

    if a == b:
        return a
    
    if a < b:
        return sum( i for i in range(a,b+1))

    if a > b:
        return sum( i for i in range(b,a+1))