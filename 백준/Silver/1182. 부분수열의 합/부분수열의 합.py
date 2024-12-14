import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums = list(map(int,input().split()))
count = 0
answer = []

def check_sum(start):
    global count

    if sum(answer) == S and len(answer)>0:
        count += 1

    for i in range(start,N):
        answer.append(nums[i])
        check_sum(i+1)
        answer.pop()


check_sum(0)
print(count)






