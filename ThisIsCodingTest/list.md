
## time = 35m/40m
- 테스트케이스는 맞았는데 다른 테케는 틀릴 가능성 엄청 높은 엉성한 내 풀이 ...
- 답안 퀄리티에 비해 훨씬 떨어진다

## info
1. 기존의 떡이 19 15 10 17 길이라고 하면
2. 절단기가 k일때
3. 손님은 19-k, 15-k, 10-k, 17-k 만큼 가져감
    - 원래 떡의 길이 < k면 못가져감
4. 손님이 요청한 m이상의 길이를 가져가게 하기 위해
5. 절단기의 길이를 얼마로 설정?

## Logic
#### 이상한 내 풀이
- 19 15 10 17
- 0 6 21 2 -> 각자의 길이로 자른 리스트
- 0 2 6 21 -> 위에거 소팅
- 원하는게 6이면
    - 2번 리스트의 6인 인덱스 리턴
    - 그 인덱스의 1번 리스트 값 리턴
- 원하는게 8이면
    - 6 ~ 21 사이
    - 작은거는 6
    - 3번 리스트에서 6의 인덱스는 2
    - 2번 리스트의 6의 인덱스는 1
    - 1번 리스트의 1 인덱스는 15
    - 기준 8 < 6 + (2+1)* i
    - 가 되는 i를 찾아서 15 + i
### 답지 풀이
1. 파라메트릭 서치: 원하는 조건을 만족하는 가장 알맞은 값
    - => 이진 탐색 사용!
    