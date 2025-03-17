def solution(t, p):

    len_p = len(p)
    num_p = int(p)
    count = 0
    
     #슬라이딩 윈도우
    for i in range(len(t) - len_p + 1):  
        sub = t[i:i+len_p]  
        if(int(sub)<= num_p):
            count+=1
                    
    return count