n = int(input())

dp = [-1] * 1001

dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, n+1):
  if dp[i-1] == 0 or dp[i-3] == 0:
      dp[i] = 1
  else:
      dp[i] = 0

if dp[n] == 1:
    print("SK")
else:
    print("CY")