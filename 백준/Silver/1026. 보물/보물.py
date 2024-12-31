import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()
result = 0

#arr1의 최소x arr2의 최대
for i in range(N):
    a = arr1[i]
    b = arr2.pop(arr2.index(max(arr2)))
    result += a*b

print(result)