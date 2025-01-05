import sys
input = sys.stdin.readline

result = []  

while True:
    num = input().strip() 
    if num == '0': 
        break
    if num == num[::-1]: 
        result.append('yes')
    else:
        result.append('no')

print(*result, sep="\n")

