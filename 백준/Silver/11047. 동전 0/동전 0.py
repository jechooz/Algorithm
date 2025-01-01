import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)


coins.sort(reverse=True)
count = 0

for i in range(n):
    if k >= coins[i]:
        count += k //coins[i]
        k %= coins[i]

    if k == 0:
        break

print(count)
        