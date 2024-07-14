def solution(my_string, overwrite_string, s):
    overwrite_length = len(overwrite_string)
    result = list(my_string)
    
    for i in range(overwrite_length):
        result[s + i] = overwrite_string[i]
    
    return ''.join(result)