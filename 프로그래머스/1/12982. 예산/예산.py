def solution(d, budget):
    answer = 0
    count = 0
    budgetresult=budget
    
    d.sort()
    
    for i in d:
        if budgetresult-i>=0:
            budgetresult=budgetresult-i
            count+=1
    
    return count