import sys

n, k = map(int,sys.stdin.readline().split())
dp = [k+1]*(k+1)
dp[0] = 0
coin = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp <= k:
        coin.append(tmp)
        dp[tmp] = 1

for i in range(1, k+1):
    if dp[i]==1:
        continue
    else:
        for c in coin:
            if i > c:
                if dp[i-c] != k+1:
                    dp[i] = min(dp[i], 1+dp[i-c])

if dp[k] != k+1: print(dp[k])
else: print(-1)
