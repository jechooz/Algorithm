def solution(myString, pat):
    answer = 0
    m=myString.lower()
    p=pat.lower()
    
    if p in m:
        return 1 
    else:
        return 0
    