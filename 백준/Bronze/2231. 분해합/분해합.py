n = input()
target = int(n)
begin = max(target - 9*len(n), 0)
candidates = []
for i in range(begin, target):
    if target == sum(map(int, str(i))) + i:
        candidates.append(i)
if len(candidates) == 0:
    print(0)
else:
    print(min(candidates))