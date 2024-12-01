arr = []
a,b=0,0
for _ in range(9):
    arr.append(int(input()))
    
total= sum(arr) 

for i in range(9):
    for j in range(i+1,9):
        if total - (arr[i]+arr[j])==100:
            a= arr[j]
            b= arr[i]
            break
            

arr.remove(a)
arr.remove(b)
arr.sort()

print(' '.join(map(str,arr)))

