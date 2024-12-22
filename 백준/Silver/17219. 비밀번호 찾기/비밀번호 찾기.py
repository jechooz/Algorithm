import sys
input = sys.stdin.readline

N,M = map(int,input().split())

dic = {}

for _ in range(N):
    site, password = input().split()
    dic[site] = password
    

for _ in range(M):
    find_site = input().strip()
    print(dic[find_site])


     
        
    

