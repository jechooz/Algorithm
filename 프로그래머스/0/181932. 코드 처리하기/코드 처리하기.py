def solution(code):
    if not code:
        return "EMPTY"
    
    ret = ''
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 0 if mode ==1 else 1  # mode 변경
            continue
        
        if mode == 0:
            if idx % 2 == 0:
                ret += code[idx]
        
        elif mode == 1:
            if idx % 2 == 1:
                ret += code[idx]
    
    # 반복문이 끝난 후 ret이 비어있으면 "EMPTY"를 반환
    return ret if ret else "EMPTY"
    
     