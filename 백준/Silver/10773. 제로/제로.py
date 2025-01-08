import sys
input = sys.stdin.readline

m = int(input())
stack = []
for _ in range(m):
    n = int(input())
    if n == 0:			
        stack.pop()		
        continue
    stack.append(n)		
print(sum(stack))