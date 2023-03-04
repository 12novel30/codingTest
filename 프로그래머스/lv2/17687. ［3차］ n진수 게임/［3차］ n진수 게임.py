def solution(n, t, m, p):
    tmp = []
    limit = p+(t-1)*m
    start = 0
    while len(tmp) <= limit:
        tmp+=list(convert_notation(start, n))
        start+=1
    
    answer = ''
    for i in range(t):
        answer += tmp[p+i*m-1]
    return answer


'''
순서는 p번 , n명
p, p+n, p+2n ... 이 t번 -> 최대는 p+(t-1)n -> 까지 리스트가 차면 멈출것


'''
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return convert_notation(q, base) + T[r] if q else T[r]