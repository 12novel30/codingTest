# 코테 준비중
def solution(citations):
    answer = 1
    citations.sort()
    if citations[0] > len(citations): return len(citations) 
    for c in reversed(citations):
        if c >= answer: answer += 1
        else: return answer - 1
    
    return answer

'''
0 1 2 5 6 -> 2
5 4 3 2 1

0 1 3 5 6 -> 3
5 4 3 2 1

0 1 4 5 6 -> 3
5 4 3 2 1
'''