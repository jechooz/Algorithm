def solution(absolutes, signs):
    answer = 0
    
    for i in range(0,len(absolutes)):
        if signs[i]:
            answer+=absolutes[i]
        else:    
            answer-=absolutes[i]
        
    return answer

# 다른 풀이    
# def solution(absolutes, signs):
#     answer=0
#     for absolute,sign in zip(absolutes,signs):
#         if sign:
#             answer+=absolute
#         else:
#             answer-=absolute
#     return answer
