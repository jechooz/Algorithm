import math

def solve():
    N = int(input())  
    A = list(map(int, input().split()))  
    X = int(input())  
    
    total_sum = 0
    count = 0
    
    for num in A:
        if math.gcd(X, num) == 1:
            total_sum += num
            count += 1
    
    average = total_sum / count
    print(f"{average:.6f}")

solve()