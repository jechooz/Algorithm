def solution(n):

    #Str(), resverse() map() int() 활용
    
    #1.정수를 스트링변경 리스트묶음
    arr=list(str(n))
    
    #2.리버스
    arr.reverse()
    
    #3.정수로 변경
    return list(map(int,arr))