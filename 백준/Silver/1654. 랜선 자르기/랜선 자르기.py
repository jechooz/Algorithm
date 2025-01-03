import sys
input = sys.stdin.readline

#가진 개수,필요 개수
k, n = map(int,input().split())
arr = []

for _ in range(k):
    arr.append(int(input()))

low = 1
high = max(arr)

while low <= high:
    mid = (low + high)//2
    count = 0
    for i in arr:
        count += i //mid
    if count >= n:
        low = mid + 1
    else:
        high = mid - 1


print(high)
