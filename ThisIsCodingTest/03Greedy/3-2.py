# 실전문제

# 큰수의 법칙
# n번 더해 가장 큰 수 만들기
# 각 수는 연속으로는 k번의 횟수 제한이 있음

# 입력값 :
# 5 8 3 (N M K)
# 2 4 5 4 6

# 제일 큰 수 6
# 6 6 6 5 6 6 6 5가 답인듯

n, m, k = map(int, input().split())
data = list(int, input().split())
