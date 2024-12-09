
import sys
input = sys.stdin.readline

def plus_sum(n):
  dp = [0] * 11

  dp[1] = 1
  dp[2] = 2
  dp[3] = 4
  
  if n > 3:
    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
       
  return dp[n] 
        


T = int(input())
for _ in range(T):
    print(plus_sum(int(input())))
  
  