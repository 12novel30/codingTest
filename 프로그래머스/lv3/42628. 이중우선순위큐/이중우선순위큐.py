def solution(operations):
    answer = []
    
    for op in operations:
        order, num = op.split()
        if order == 'I':
            answer.append(int(num))
        elif order == 'D' and len(answer) != 0:
            if int(num) == 1:
                tmpMax = max(answer)
                answer.remove(tmpMax)
            elif int(num) == -1:
                tmpMin = min(answer)
                answer.remove(tmpMin)
    
    if len(answer) == 0: return [0,0]
    else:
        return [max(answer), min(answer)]