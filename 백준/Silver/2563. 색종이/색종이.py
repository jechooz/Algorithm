N = int(input())

paperList = []
bigPaper = [[False] * 101 for _ in range(101)]
answer = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            bigPaper[i][j] = True

for i in range(1, 101):
    for j in range(1, 101):
        if bigPaper[i][j] == True:
            answer += 1

print(answer)