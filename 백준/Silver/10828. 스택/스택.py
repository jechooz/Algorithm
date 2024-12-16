import sys
input = sys.stdin.readline

stack = []

N = int(input())
for _ in range(N):
    req = input().split()

    if req[0] == 'push':
        stack.append(req[1])
    elif req[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif req[0] == 'size':
        print(len(stack))
    elif req[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())           
        
    