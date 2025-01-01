import sys
input = sys.stdin.readline


a = input()
result = 0

arr = a.split('-')

for i in arr[0].split('+'):
    result += int(i)

for i in arr[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)
    