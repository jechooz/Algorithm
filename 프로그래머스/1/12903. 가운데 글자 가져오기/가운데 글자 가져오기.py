def solution(s):
    answer = ''
    a=len(s)
    
    #5%2=2..1     
    #01234 012
    
    #4%2=2
    #0123 12
    
    #짝수 
    if len(s)%2==0:
        return s[a//2-1:a//2+1]
    else:
        return s[a//2]
    
    return answer