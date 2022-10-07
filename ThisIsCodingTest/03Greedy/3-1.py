# 거스름돈
# 거슬러줘야 할 돈의 최소 개수
# 화폐: 10 50 100 500

N = 1260
count = 0

'''내 답
if N>=500:
    count += int(N/500)
    N = N%500

if N>=100:
    count += int(N/100)
    N = N%100

if N>=50:
    count += int(N/50)
    N = N%50

if N>=10:
    count += int(N/10)
    N = N%10
    
print(count)
'''

coin_type = [500,100,50,10]
for coin in coin_type:
    count+=int(N/coin)
    N = N%coin
print(count)