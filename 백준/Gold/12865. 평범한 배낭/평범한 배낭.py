# 0/1 knapsack

def knapsack(num,nump,numw,maxw):
    dp=[[0 for _ in range(maxw+1)] for _ in range(num+1)]
    for i in range(1, num+1):
        for j in range(1, maxw+1):
            if numw[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],
                             dp[i-1][j-numw[i-1]] + nump[i-1])
    return dp[num][maxw]

# driver code
num, maxweight=input().split()
num=int(num)
maxweight=int(maxweight)
numprofit = [0]*(num)
numweight = [0]*(num)
for i in range(num):
    numweight[i], numprofit[i]=input().split()
    numweight[i] = int(numweight[i])
    numprofit[i] = int(numprofit[i])
print(knapsack(num,numprofit,numweight,maxweight))