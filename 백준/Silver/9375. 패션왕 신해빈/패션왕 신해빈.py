import sys
input = sys.stdin.readline

case = int(input())


for _ in range(case):
    n = int(input()) 
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    result = 1
    
    for kind in clothes:
        result *= (len(clothes[kind]) + 1)

    print(result - 1)


          
        
    

