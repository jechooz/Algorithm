import sys
input = sys.stdin.readline

t = int(input())
result = 0

for _ in range(t):
    seq = input().rstrip()
    stack = []

    for ch in seq:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)

    if not stack:
        result += 1

print(result)