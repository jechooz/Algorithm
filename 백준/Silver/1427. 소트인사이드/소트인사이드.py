import sys
input = sys.stdin.readline

n = input()
arr = []

#각 자리수 담은 배열
for i in n:
    arr.append(i) 

#선택정렬
for i in range(len(arr)):
    max_index = i
    for j in range(i+1,len(arr)):
        if arr[max_index]<arr[j]:
            max_index = j
    arr[i],arr[max_index] = arr[max_index],arr[i]

print(''.join(arr))
        
    
