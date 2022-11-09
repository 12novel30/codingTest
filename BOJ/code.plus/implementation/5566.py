n, m = map(int, input().split())

instruction = []
dice = []

for i in range(n):
    instruction.append(int(input()))
for i in range(m):
    dice.append(int(input()))

now = 1
endpoint = n
count = 0

for i in range(m):
    
    tmpdice = dice[i] # 1번째 주사위
    count += 1
    now += tmpdice # 주사위로 변경된 위치
    
    if now >= endpoint:
        break
    
    tmpinst = instruction[now-1] # 옮긴 위치의 지시사항
    now += tmpinst
    
    if now >= endpoint:
        break

print(count)