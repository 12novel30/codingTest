def solution(clothes):
    
    type = {}
    for cloth in clothes:
        answer = 1
        if cloth[1] not in type:
            type[cloth[1]] = 1
        else:
            type[cloth[1]] += 1
    count = list(type.values())
    for c in count:
        answer *= c+1
    return answer-1