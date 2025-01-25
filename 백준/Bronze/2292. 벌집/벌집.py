

def solution(N):
    if N == 1:
        return 1 
    
    level = 1 
    rooms = 1  
    while rooms < N:
        rooms += 6 * level  
        level += 1  
    
    return level

N = int(input().strip())
print(solution(N))

