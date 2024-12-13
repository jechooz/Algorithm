import sys
input = sys.stdin.readline

region = int(input())
budget_requests = list(map(int,input().split()))
total_budget = int(input())

start = 0
end = max(budget_requests)

while start <= end:
  #상한액
  mid = (start + end) // 2
  sum = 0
  for request in budget_requests:
      if request <= mid:
          sum += request
      else:
          sum += mid
  if sum <= total_budget:
      start = mid + 1
  else:
      end = mid - 1

print(end)