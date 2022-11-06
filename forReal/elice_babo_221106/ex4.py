numServer = 2
logs = 	[[1, 4], [2, 5], [3, 1], [4, 6], [8, 2], [10, 4]]

def solution(numServer, logs):
    
    # rr
    rrserver = [0]*numServer
    rrserverindex = 0
    for l in logs:
        if rrserver[rrserverindex] <= l[0]:
            rrserver[rrserverindex] = l[0]+l[1]
        else:
            rrserver[rrserverindex] += +l[1]
        rrserverindex += 1
        if rrserverindex >= numServer:
            rrserverindex = 0
    print(max(rrserver))
        
    # lc
    lcserver = [(0,0)]*numServer
    lcserverindex = 0
    minhostCount = 0
    for l in logs:
        
        # 서버 중 어떤 게 제일 적은 연결이 되어있는지 찾기
        for i in range(numServer):
            if numServer[i][1] < minhostCount:
                minhostCount = numServer[i][1]
                lcserverindex = i
        
        
        
        
        
        if rrserver[rrserverindex] <= l[0]:
            rrserver[rrserverindex] = l[0]+l[1]
        else:
            rrserver[rrserverindex] += +l[1]
        rrserverindex += 1
        if rrserverindex >= numServer:
            rrserverindex = 0
    print(max(rrserver))
    
solution(numServer, logs)