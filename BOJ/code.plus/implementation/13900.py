from sys import stdin

n = int(input())
data = list(map(int, stdin.readline().rstrip().split()))
total = sum(data)
result = 0

for i in range(n):
    total -= data[i]
    result += data[i] * total

print(result)