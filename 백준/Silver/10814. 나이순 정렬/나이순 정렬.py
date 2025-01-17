import sys
input = sys.stdin.readline
n = int(input()) 
members = []

for _ in range(n):
    age, name = input().split()
    age = int(age)
    members.append((age, name))

members.sort(key=lambda x: x[0]) 

for m in members:
    print(m[0], m[1])  