def solution(box):
    
    for i in range(1, len(box)):
        if box[i-1] < box[i]:
            cha = box[i] - box[i-1]
            if cha%2!=0: deo = cha//2 + 1
            else: deo = cha//2
            box[i] -= deo
            box[i-1] += deo
    
    for i in range(len(box)-1, 0, -1):
        if box[i-1] < box[i]:
            cha = box[i] - box[i-1]
            if cha%2!=0: deo = cha//2 + 1
            else: deo = cha//2
            box[i] -= deo
            box[i-1] += deo

    
    return max(box)