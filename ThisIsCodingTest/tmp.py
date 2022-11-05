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