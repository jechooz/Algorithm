import sys
input = sys.stdin.readline

stack = []
N = input().strip()
count = 0

for i in range(len(N)):
    if N[i] == '(':
        stack.append(N[i])
    else: #)
        if i > 0 and N[i-1] == '(':
            stack.pop()
            count += len(stack)
        else: 
            stack.pop()
            count +=1



print(count)