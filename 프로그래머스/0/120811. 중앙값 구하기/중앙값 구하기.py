def solution(array):
    array.sort()
    #array = sorted(array)
    length = len(array)//2
    return array[length]