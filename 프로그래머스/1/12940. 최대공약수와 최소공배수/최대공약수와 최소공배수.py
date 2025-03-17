def solution(n, m):
    answer = []
    lcm = 0

    gcd_val = gcd(m,n)
    lcm_val = (n * m) // gcd_val 
    answer.append(gcd_val)
    answer.append(lcm_val)
    return answer
        

def gcd(a,b):
    
    if a % b == 0:
        return b
    
    return gcd(b,a%b)
   