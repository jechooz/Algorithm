import sys
input = sys.stdin.readline

def cnt(document, word):
    count = 0
    pos = 0
    
    while True:
        pos = document.find(word, pos)
        
        if pos == -1:
            break
        
        count += 1
        pos += len(word)
    
    return count

document = input().strip()
word = input().strip()

print(cnt(document, word))