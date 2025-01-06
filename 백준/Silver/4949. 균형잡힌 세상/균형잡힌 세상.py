import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    stack = []

    if n == '.':
        break
    
    for i in n:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if len(stack) != 0:
        print('no')
    else:
        print('yes')


