import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    while K > scoville[0]:
        if len(scoville) < 2:
            return -1
        first = hq.heappop(scoville)
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1
    
    return answer