import sys
input = sys.stdin.readline

n = int(input())
count_two = 0
count_five = 0

for i in range(1, n + 1):
    temp = i
    while temp %2 == 0:
        temp //= 2
        count_two += 1
    while temp %5 == 0:
        temp //= 5
        count_five += 1

print(min(count_two, count_five))
