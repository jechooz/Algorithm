import sys
input = sys.stdin.read

def solution():
    data = input().splitlines()  
    N = int(data[0]) 
    points = []

    for i in range(1, N + 1):
        x, y = map(int, data[i].split())
        points.append((x, y))

    # y 기준 정렬
    points.sort(key=lambda point: (point[1], point[0]))

    for point in points:
        print(point[0], point[1])


solution()