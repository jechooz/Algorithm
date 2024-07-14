def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if n%2 == 0:
            if i%2==0:
                answer+= i**2
        else: 
            if i%2==1:
                answer+= i
                
    return answer            
                
    '''다른 풀이
    def solution(n):
    if n % 2:  # n이 홀수일 경우
        return sum(range(1, n+1, 2))  # n 이하의 홀수들의 합을 반환
    else:  # n이 짝수일 경우
        return sum([i*i for i in range(2, n+1, 2)])  # n 이하의 짝수들의 제곱의 합을 반환


   n % 2가 0이 아닌 값 (즉, 1이나 -1 등) 일 경우, 조건식은 참(True)으로 간주.이는 n이 홀수일 때와 같은 결과
   n % 2가 0일 경우, 조건식은 거짓(False)으로 간주됩니다. 이는 n이 짝수인 경우와 같은 결과

    '''
