import math


def solution(n):
        #6과 n의 최소공배수 구하기
        #최소공배수는 두 수의 곱을 두 수의 최대공약수(GCD)로 나눔
        # 두 수를 모두 나눌 수 있는 최소한의 조각 수
    lcm = n * 6 // math.gcd(n, 6)
    return lcm // 6