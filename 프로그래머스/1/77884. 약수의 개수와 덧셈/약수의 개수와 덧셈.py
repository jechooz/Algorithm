def solution(left, right):
    answer = 0

    
    for i in range(left,right+1):
        lenx=0
        
        for j in range(1,i+1):
            if i%j==0:
                lenx+=1
                
        if lenx % 2 ==0:
            answer+=i
        if lenx %2==1:
            answer-=i
                
        
        
    return answer
    
    
   