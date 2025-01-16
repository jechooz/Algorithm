
def solution(arr):
    for i in range(1, len(arr)):  
        key = arr[i]  
        j = i - 1  
      
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
     
        arr[j + 1] = key


N = int(input())  
numbers = list(map(int, input().split()))
unique = list(set(numbers))
solution(unique)


print(" ".join(map(str, unique)))