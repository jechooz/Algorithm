
#퀵정렬
def quick_sort(arr):
  if len(arr)<=1:
    return arr
  pivot = arr[len(arr)//2]
  left = [x for x in arr if x<pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x>pivot]
  return quick_sort(left)+middle+quick_sort(right)


#기차 인원 배열
maxP = 0
arr = []

for _ in range(10):
    a,b = map(int,input().split())
    maxP += - a+b
    arr.append(maxP)
  
  
arr = quick_sort(arr)
print(arr[-1])