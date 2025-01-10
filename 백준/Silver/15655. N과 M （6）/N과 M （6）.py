import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

def dfs(start):
    if len(result) == m:
        for i in range(m):
            print(result[i], end=' ')
        print('')
        return
    for i in range(start, n):
        if arr[i] in result:
            continue
        
        result.append(arr[i])
        dfs(i)  
        result.pop()

        
arr.sort()
dfs(0)

            