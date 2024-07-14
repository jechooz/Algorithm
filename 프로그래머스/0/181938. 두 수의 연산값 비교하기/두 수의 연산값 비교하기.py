def solution(a, b):
    result = 0
    result = int(str(a) + str(b))  # a ⊕ b 계산
        
    if  result >= 2 * a * b:
        return result
    elif result < 2 * a * b:  
        return 2 * a * b


```python
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

```

    
    

                  
                  
