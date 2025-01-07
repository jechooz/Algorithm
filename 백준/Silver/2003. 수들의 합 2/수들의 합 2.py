n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
current_sum = 0
count = 0

while True:
    if m <= current_sum:
        current_sum -= arr[left]
        left += 1
    else:
        if right == n:
            break
        current_sum += arr[right]
        right += 1

    if current_sum == m:
        count += 1

print(count)
