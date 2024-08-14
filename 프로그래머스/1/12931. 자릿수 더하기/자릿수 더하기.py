def solution(number):

    arr= list(str(number))
    answer = sum(int(i) for i in arr)
    
    return answer
    