N = map(int, input().split())

A =set(map(int, input().split()))
B = set(map(int, input().split()))

result = []
for n in A:
    if n not in B:
        result.append(n)

result.sort()
print(len(result))

if len(result) !=0:
    print(*(result))