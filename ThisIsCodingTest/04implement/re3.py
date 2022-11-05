'''실전 3 게임 개발

## time = 시간 초과/40m & 답지 봤음 ㅜㅜ

## info
1. 맵 안에서 벗어날 수 없음
2. 현재 방향을 기준으로, 반시계 방향부터 차례대로 갈 곳을 정함
    - 방향: 
3. 해당 방향에, 안가본 칸이 있으면 한 칸 전진
    - 다 가봤으면 continue
4. 전부 다 가본 방향/바다면
    1. 방향유지, 한칸 뒤로
    2. 바다면 stop
5. 리턴: 캐릭터가 방문한 칸의 개수

## Logic
1. while
    1. 현재 칸을 1로 변경 & count++
    2. for i in range(4)
        2. 방향 변경 *** <- 답지 본 부분 ㅜㅜ 새로운 함수 작성!
            - with global variable
        3. 변경한 방향에 있는 칸이 0이면 이동 -> count++ & break
        4. 변경한 방향에 있는 칸이 1이면 -> continue
    3. 방향 바꾼 뒤 이동할 수 있으면 그 다음 단계로
    4. 방향 바꿔도 이동할 수 없는 경우(if 모든 방향 다 체크)
        - 현재 방향에서 한칸 뒤가 1이면 break
        - 현재 방향에서 한칸 뒤가 0이면 뒤로 이동 -> count++ & continue
'''

n,m = map(int, input().split()) # 3<=n, m<=50
x, y, nowDir = map(int, input().split())
place = []
for i in range(n):
    place.append(list(map(int, input().split())))

count = 0
def turn_left(): # 몰라서 답지 봤음 ㅠㅠ
    global nowDir
    nowDir -= 1
    if nowDir == -1:
        nowDir = 3
step = [(-1,0), (0,1), (1,0), (0,-1)] # N, E, S, W

while True:
    place[x][y] = 1
    count += 1
    
    for i in range(4):
        turn_left()
        # 새로운 방향으로 갈 수 있는가?
        nx = x + step[nowDir][0]
        ny = y + step[nowDir][1]
        nplace = place[nx][ny]
                      
        if place[x + step[nowDir][0]][y + step[nowDir][1]] == 0: # 있으면 현위치 변경
            x = x + step[nowDir][0]
            y = y + step[nowDir][1]
            break
        else: continue # 없으면 다음 방향 체크
    if place[x][y] == 0:
        continue # 방향 바꾼 뒤 이동할 수 있으면 그 다음 단계로!
    
    # 방향 바꿔도 이동할 수 없는 경우
    if place[x - step[nowDir][0]][y - step[nowDir][1]] == 0:
        x = x - step[nowDir][0]
        y = y - step[nowDir][1]
    else: break

print(count)

'''
inpnt
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''