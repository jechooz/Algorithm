def solution(number):

    #문자열화->리스트화
    arr=list(str(number))
    
    return sum(int(i) for i in arr)
    