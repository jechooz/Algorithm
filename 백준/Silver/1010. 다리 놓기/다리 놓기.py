T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[1] = [i for i in range(M + 1)]

    for n in range(2, N + 1):
        for m in range(1, M + 1):
            dp[n][m] = sum(dp[n - 1][m - i] for i in range(1, m + 1))

    print(dp[N][M])