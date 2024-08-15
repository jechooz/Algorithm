def solution(s):
    
    a=len(s)
    
    #짝수 
    if len(s)%2==0:
        return s[a//2-1:a//2+1]
    else:
        return s[a//2]
    
