def solution(n):
    #7의 배수라면 몫반환
    #7배수가 아니라면 몫+1
    
    #<참일 때 값> if <조건> else <거짓일 때 값>
    #n % 7이 0이 아니면 (n % 7이 참이면), n // 7 + 1을 반환
    #n % 7이 0이라면 else 뒤의 n // 7
    
    answer = n//7+1 if n%7 else n//7
    return answer