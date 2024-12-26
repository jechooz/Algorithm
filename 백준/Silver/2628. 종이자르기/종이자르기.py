w, h = map(int, input().split())
c = int(input())

ww = [0, w]
hh = [0, h]

for _ in range(c):
    d, p = map(int, input().split())
    if d == 0:
        hh.append(p)
    else:
        ww.append(p)

ww.sort()
hh.sort()

wws = []
hhs = []

for i in range(len(ww)-1):
    wws.append(ww[i+1] - ww[i])

for i in range(len(hh)-1):
    hhs.append(hh[i+1] - hh[i])

print(max(wws) * max(hhs))
