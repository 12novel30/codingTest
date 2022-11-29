import sys

t = int(sys.stdin.readline())
answer = []
for i in range(t):
    data = []
    n = int(sys.stdin.readline())
    
    if n==1:
        tmp1 = int(sys.stdin.readline())
        tmp2 = int(sys.stdin.readline())
        answer.append(max(tmp1, tmp2))
    else:
        data.append(list(map(int,sys.stdin.readline().split())))
        data.append(list(map(int,sys.stdin.readline().split())))
        if n==2:
            answer.append(max(data[0][0]+data[1][1],data[0][1]+data[1][0]))
        else:
            dp = [[data[0][0], data[0][1]+data[1][0]],
                  [data[1][0], data[0][0]+data[1][1]]]
            for j in range(2, n):
                for i in range(2):
                    tmp1 = data[i][j]
                    tmp2 = dp[1-i][j-1]
                    tmp3 = dp[1-i][j-2]
                    dp[i].append(data[i][j] + max(dp[1-i][j-1], dp[1-i][j-2]))
            answer.append(max(dp[0][-1], dp[1][-1]))
for ans in answer:
    print(ans)