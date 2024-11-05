import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    ##분자
    numer = numer1*denom2 + numer2*denom1
    
    ##분모
    denom = denom1*denom2
    
    ##최대공약수로 약분
    gcd = math.gcd(denom,numer)
    
    #분모,분자 배열
    return [numer//gcd, denom//gcd]