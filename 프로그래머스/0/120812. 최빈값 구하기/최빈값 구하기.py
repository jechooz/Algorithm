def solution(array):
    
    #enumerate로 배열의 값을 인덱스와 함께 추출해서 반복
    while len(array) != 0:
        for i,a in enumerate(set(array)):
            array.remove(a)
        if i ==0: 
            return a
    return -1