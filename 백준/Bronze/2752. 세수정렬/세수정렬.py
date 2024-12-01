a,b,c = map(int,input().split())
arr=[a,b,c]


for i in range(3):
    for j in range(0,3-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
for k in arr:
    print(k, end = " ")
