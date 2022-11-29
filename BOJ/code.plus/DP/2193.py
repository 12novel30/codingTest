'''
1
10

101
100
1010 마지막이 1이면 1개 추가
1000
1001 마지막이 0이면 2개 추가
'''
import sys

dp = [0,1,1]
n = int(sys.stdin.readline())
for i in range(3,n+1):
    dp.append(dp[i-1] + dp[i-2])
print(dp[n])

