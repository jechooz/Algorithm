def solution(num, n):
    return 1 if num%n==0 else 0


```다른 풀이
def solution(num, n):
    return int(num % n == 0)

num % n == 0은 num이 n의 배수일 때 참(True)이고, 그렇지 않을 때 거짓(False)
int() 함수를 사용하여 참(True)일 때 1, 거짓(False)일 때 0을 반환

```
