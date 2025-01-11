import sys
input = sys.stdin.readline

def solution1(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def solution2(x, y):
    return x * y // solution1(x, y)

num1, num2 = map(int, input().split())

answer1 = solution1(num1, num2)
print(answer1)

answer2 = solution2(num1, num2)
print(answer2)
