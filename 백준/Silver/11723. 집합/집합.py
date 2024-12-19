import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    orders = input().strip().split()
    if len(orders) == 1:
        if orders[0] == 'empty':
            S = set()
        else:
            S = set(list(range(1, 21)))
    else:
        command, num = orders[0], int(orders[1])
        if command == "add":
            S.add(num)
        elif command == "remove":
            S.discard(num)
        elif command == "check":
            print(1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)
