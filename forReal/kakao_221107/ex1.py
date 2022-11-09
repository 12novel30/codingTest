# 5/15
def solution(box):
    # Write your code here
    answer = 0
    sumBBang = sum(box)
    if sumBBang%len(box)==0:
        maxBBang = sumBBang//len(box)
    else:
        maxBBang = sumBBang//len(box) + 1
    
    if box[0] >= maxBBang:
        answer = box[0]
    else: answer = maxBBang

    return answer