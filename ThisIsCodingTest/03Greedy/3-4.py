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

## 아래가 더 좋은 풀이
# : 일일이 1을 빼는 것이 비효율적이다!
n, k = map(int, input().split())
answer = 0

while n!=1:
    if n%k == 0:
        n  /= k
        answer +=1
    else:
        if n>k:
            answer += n%k
            n -= n%k
        else:
            answer += n%k -1
            n -=n%k -1
        
    
print(answer)