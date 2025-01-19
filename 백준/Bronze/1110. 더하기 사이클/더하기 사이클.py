def cycle(n):
    original = n  
    count = 0
    
    while True:
        count += 1
        n = (n % 10) * 10 + (n // 10 + n % 10) % 10
        if n == original:
            break
    
    return count

n = int(input())
print(cycle(n))