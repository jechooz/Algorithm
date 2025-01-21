import sys
m = int(sys.stdin.readline())
numbers = []
for _ in range(m):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

total_diff = 0
for i in range(1, m+1):
    total_diff += abs(i - numbers[i-1])

print(total_diff)
