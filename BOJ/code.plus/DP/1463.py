import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
dp[0] = 0
dp[1] = 0

for i in range(2, n+1):
    tmp1, tmp2, tmp3 = i,i,i
    if i%3 == 0:
        tmp1 = dp[i//3] + 1
    if i%2 == 0:
        tmp2 = dp[i//2] + 1
    tmp3 = dp[i-1] + 1
    
    dp[i] = min(tmp1, tmp2, tmp3)

print(dp[n])