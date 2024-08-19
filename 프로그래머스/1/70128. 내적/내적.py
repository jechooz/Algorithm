def solution(a, b):
    answer = 0
    
    for ax,bx in zip(a,b):
        answer+= ax*bx
        
    return answer