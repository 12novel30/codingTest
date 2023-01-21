def solution(n, times):
    times.sort()
    start = 0
    end = times[0]*n
    
    while start <= end:
        mid = (start + end) // 2
        
        done = 0
        for t in times:
            done += mid // t
        
        if done >= n:
            end = mid -1
        elif done < n:
            start = mid + 1
            
    return start