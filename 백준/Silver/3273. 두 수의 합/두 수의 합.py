import sys
input = sys.stdin.readline
n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
left, right = 0, n-1 
while left < right:
    total = numbers[left] + numbers[right]
    if total == x:
        answer += 1
        left += 1
    elif total < x:
        left += 1
    else:
        right -= 1
print(answer)