# 순차 탐색

data = input().split()
n = int(data[0])
target = data[1]

hand = input().split()

def sequential_search(n, target, hand):
    for i in range(n):
        if hand[i] == target:
            return i+1

print(sequential_search(n, target, hand))