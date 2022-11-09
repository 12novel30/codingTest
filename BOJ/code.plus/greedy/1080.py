from sys import stdin

n, m = map(int, stdin.readline().split()) # stdin으로 변경
aMatrix = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
bMatrix = [list(map(int, stdin.readline().rstrip())) for _ in range(n)]
answer = 0

def filp_matrix(i, j):
    for p in range(i, i+3):
        for q in range(j, j+3):
            aMatrix[p][q] = 1 - aMatrix[p][q] # 간략하게

for i in range(n-2):
    for j in range(m-2):
        if aMatrix[i][j] != bMatrix[i][j]:
            filp_matrix(i, j)
            answer += 1
    # if aMatrix[i] != bMatrix[i]:
    #     answer = -1
    #     break
        if aMatrix == bMatrix:
            break
    if aMatrix == bMatrix:
        break

if aMatrix != bMatrix:
    print(-1)
else:
    print(answer)