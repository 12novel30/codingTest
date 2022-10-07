'''
22-09-06
'''

# 큰수의 법칙
# n번 더해 가장 큰 수 만들기
# 각 수는 연속으로는 k번의 횟수 제한이 있음

# 입력값 :
# 5 8 3 (N M K)
# 2 4 5 4 6

# 제일 큰 수 6
# 6 6 6 5 6 6 6 5가 답인듯

'''
@author 12nov
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

three = max(data)
data[data.index(three)] = 0
if m<4:
    print(three * m)
else:
    q = int(m/4)
    r = m%4
    one = max(data)
    print(three*(3*q+r) + one*q)

''' answer
data.sort()
first = data[n-1]
second = data[n-2]
'''