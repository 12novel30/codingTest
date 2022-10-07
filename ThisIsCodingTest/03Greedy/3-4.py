'''22-09-06 tue
[실전문제] 1이 될 때 까지 <fin>

n-1 or n/k -> n=1
min count

25 5 -> 2
17 4 -> -1 /4 /4
'''

n, k = map(int, input().split())
count = 0
while n>1:
    if n%k==0:
        n = int(n/k)
    else:
        n -= 1
    count += 1

print(count)