def solution(s):
    sList = s.split(" ")
    answer = []
    
    for i in range(len(sList)):
        sList[i] = sList[i][:1].upper() + sList[i][1:].lower()
    answer = ' '.join(sList)
    return answer