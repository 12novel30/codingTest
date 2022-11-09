n = int(input())
hand = list(map(int, input().split()))
hand.sort()
count = 0

for i in range(n):
    count += hand[i] * (n-i)
    # print(count)

print(count)