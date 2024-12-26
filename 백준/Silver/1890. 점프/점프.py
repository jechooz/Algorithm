import sys
input = sys.stdin.readline


def solution(n):
    for i in range(n):
        for j in range(n):
            if i == n - 1 and j == n - 1:
                return dp[i][j]

            jump = board[i][j]

            if i + jump < n:
                dp[i + jump][j] += dp[i][j]
            if j + jump < n:
                dp[i][j + jump] += dp[i][j]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

print(solution(N))
