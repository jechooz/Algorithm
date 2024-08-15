def solution(x):
    answer = True
    
    arr=list(str(x))
    xplus = sum(int(i) for i in arr)
    
    return x%xplus==0