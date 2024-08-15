def solution(x):
    answer = True
    
    arr=list(str(x))
    xplus = sum(int(i) for i in arr)
    
    return x%xplus==0


```python 다른풀이

def sum_of_integers_between(start, end):
    # start가 end보다 크면 두 값을 바꿈
    if start > end:
        start, end = end, start
    
    # range 함수는 start부터 end까지의 정수 범위를 생성.
    # end + 1을 사용하는 이유는 range 함수가 end 값을 포함하지 않기때문.
    return sum(range(start, end + 1))

```
