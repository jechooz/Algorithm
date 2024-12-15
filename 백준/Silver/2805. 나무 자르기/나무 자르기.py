import sys
input = sys.stdin.readline

N,M = map(int,input().split())
trees = list(map(int,input().split()))

trees.sort()
start = 0
end = max(trees)

def binary_search(trees,M,start, end):

    while start <= end:
        total = 0
        mid = (start+end) // 2

        for tree in trees:
            if tree> mid:
                total += tree - mid


        if total >= M:
                start = mid + 1
        else: 
                end = mid -1


    return end


result = binary_search(trees, M, start,end)
print(result)
        
    
        
    