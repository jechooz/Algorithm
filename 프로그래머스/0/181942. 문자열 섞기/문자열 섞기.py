def solution(str1, str2):
    answer = ''
    list1=list(str1)
    list2=list(str2)
    
    for i in range(0,len(str1)):
        answer+=list1[i]
        answer+=list2[i]
    
    return answer