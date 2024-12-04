import sys
input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checkCards = list(map(int, input().split()))

# 카드개수 세기
card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

# 이진 탐색 함수 
def bSearch(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return card_count[target]
    elif arr[mid] > target:
        return bSearch(arr, target, start, mid - 1)
    else:
        return bSearch(arr, target, mid + 1, end)


for checkCard in checkCards:
    print(bSearch(cards, checkCard, 0, len(cards) - 1), end=' ')