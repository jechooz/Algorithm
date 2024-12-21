import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = [input().strip() for _ in range(N)]

w_board = []
for i in range(8):
    row = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row += "W"
        else:
            row += "B"
    w_board.append(row)

b_board = []
for i in range(8):
    row = ""
    for j in range(8):
        if (i + j) % 2 == 0:
            row += "B"
        else:
            row += "W"
    b_board.append(row)

min_changes = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        count_w = 0
        count_b = 0
        for r in range(8):
            for c in range(8):
                if chess[i + r][j + c] != w_board[r][c]:
                    count_w += 1
                if chess[i + r][j + c] != b_board[r][c]:
                    count_b += 1
        min_changes = min(min_changes, count_w, count_b)

print(min_changes)