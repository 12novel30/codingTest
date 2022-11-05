''' 예제 4-1 상하좌우
## info
1. LRUD 4가지 액션
2. NXN을 벗어나는 움직임은 "무시"
3. 좌표 시작은 (1,1)

## Logic
1. 초기 c좌표 = 1
2. 초기 r좌표  = 1
3. L: r-1
4. R: r+1
5. U: c+1
6. D: c-1
7. 제한: if r>= 5 or c>=5: 액션 무시
'''

n = int(input())
# action = list(input().split()) -> 이렇게 안해도 된다
action = input().split()
c,r = 1,1
afterC, afterR = c, r

for act in action:
    if act.__eq__('L'):
        afterC = c-1
    if act.__eq__('R'):
        afterC = c+1
    if act.__eq__('U'):
        afterR = r-1
    if act.__eq__('D'):
        afterR = r+1
    
    if afterC < n and afterC > 0 and afterR < n and afterR > 0:
        c = afterC
        r = afterR

print(str(r)+" "+str(c))