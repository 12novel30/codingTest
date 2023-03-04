def solution(rows, columns, queries):
    mat = [[] for i in range(rows)]
    start = 1
    for i in range(rows):
        for j in range(columns):
            mat[i].append(start)
            start += 1
    
    answer = []
    for q in queries:
        start = mat[q[0]-1][q[1]-1]
        mini = start
        for c in range(q[1], q[3]):
            mat[q[0]-1][c], start = start, mat[q[0]-1][c]
            mini = min(mini, start)
        for r in range(q[0], q[2]):
            mat[r][q[3]-1], start = start, mat[r][q[3]-1]
            mini = min(mini, start)
        for c in range(q[3]-2, q[1]-2, -1):
            mat[q[2]-1][c], start = start, mat[q[2]-1][c]
            mini = min(mini, start)
        for r in range(q[2]-2, q[0]-2, -1):
            mat[r][q[1]-1], start = start, mat[r][q[1]-1]
            mini = min(mini, start)
        answer.append(mini)
    
    return answer