# 코테 준비로 다시 풀었음
def solution(clothes):
    dict = {}
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = 1
        else:
            dict[cloth[1]] += 1
    answer = 1
    for v in dict.values():
        answer *= v+1
    return answer - 1