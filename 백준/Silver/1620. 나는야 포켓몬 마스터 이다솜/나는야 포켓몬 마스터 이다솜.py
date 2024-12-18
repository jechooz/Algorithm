import sys
input = sys.stdin.readline

N,M = map(int,input().split())
call_id = {}
call_word = {}

for i in range(1,N+1):
    pok = input().strip()
    call_id[i] = pok 
    call_word[pok] = i

for _ in range(1,M+1):
    m = input().strip()
    if m.isalpha():
        print(call_word[m])
    else:
        print(call_id[int(m)])
      