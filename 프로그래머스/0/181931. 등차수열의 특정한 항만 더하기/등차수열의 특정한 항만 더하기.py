def solution(a, d, included):
    answer = 0
    list = [ a + d *i for i in range(len(included))]
    
    for i in range(len(included)):
        if included[i] :
            answer += list[i]
    
    return answer
            