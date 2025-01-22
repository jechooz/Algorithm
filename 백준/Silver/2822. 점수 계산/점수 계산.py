import sys
input = sys.stdin.readline
score = []
result = []
total = 0
for _ in range(8):
    score.append(int(input()))
    
for _ in range(5):
    total += max(score)
    idx = score.index(max(score))
    result.append(idx+1)
    score[idx] = 0
result.sort()
print(total)
print(*result)
    