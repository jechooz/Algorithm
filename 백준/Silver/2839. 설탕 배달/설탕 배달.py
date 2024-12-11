def min_bags(N):
    for i in range(N // 5, -1, -1):
        remaining = N - (i * 5)
        if remaining % 3 == 0:
            return i + remaining // 3
    return -1

N = int(input())
print(min_bags(N))