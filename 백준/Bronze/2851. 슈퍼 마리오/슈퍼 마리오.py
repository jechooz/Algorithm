import sys
input = sys.stdin.readline

m= []
total = 0
closest = 0
for _ in range(10):
    m.append(int(input().strip()))


for i in range(10):
    total += m[i]

    if abs(total - 100) < abs(closest - 100):
        closest = total
    elif abs(total - 100) == abs(closest - 100):
        closest = max(closest, total)


print(closest)

