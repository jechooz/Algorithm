def solution(s):
    dic = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
    
    word = ''
    answer = ''
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            word += i
            if word in dic:
                answer += str(dic[word])
                word = ''

                
    return int(answer)       
            