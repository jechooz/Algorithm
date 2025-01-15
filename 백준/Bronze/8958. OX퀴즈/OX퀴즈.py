t = int(input())

for _ in range(t):
    result = input().strip()  
    
    total_score = 0  
    cnt = 0 
    
    for answer in result:
        if answer == 'O':
            cnt += 1  
            total_score += cnt  
        else:
            cnt = 0  
    
    print(total_score)  