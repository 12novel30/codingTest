def solution(citations):
    citations.sort()
    count = []
    tmpCount = 0
    isAllZero = True
    for i in range(len(citations)):
        # [0,0,0,0,0] 예외 처리를 위함
        if citations[i] != 0: isAllZero = False
        
        if i == 0 or citations[i] != citations[i-1]:
            tmpCount = len(citations[i:])
        count.append(tmpCount)
        
        if citations[i] >= count[i]:
            return count[i]
    
    if isAllZero == True: return 0