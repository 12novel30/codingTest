n,k = map(int, input().split())
bill = []
for i in range(n):
    bill.append(int(input()))
count = 0

for i in range(n-1, -1, -1):
    
    if k == 0:
        break
    
    count += k//bill[i]
    k %= bill[i]
    # print(k)

print(count)