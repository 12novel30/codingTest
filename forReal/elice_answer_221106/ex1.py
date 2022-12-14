''' 코테 결과
평균 81.29
녹화본 올라온단다
나중에 문제 풀어보란다
해설 ppt는 bittersweet14123o으로 보내주신다
'''

'''1번
문자열에서 naknak을 골라내는게 쉽다
존재할 때마다 count 를 1 씩 올려준다
-> 실수한게 ... naknakna도 o였다 ㅠㅠ 바보
'''

'''2번
평균 15.2점
info 상금을 적게 하려면?

- 가장 적게 이긴 사람이 맨 뒤
- 그 다음으로 적게 이긴 사람이 그 앞
- 경기에서 승리한 횟수가 가장 큰 순서대로 나열하면 된다 ㅋㅋㅋㅋ
- 각자 경기 결과를 저장하고, 정렬하면 된다

-> 거의 맞았는데 ... 바보
-> 누가 누구한테 이겼는지 안해도 된다
'''

'''3번
평균: 6.77

- 임의의 두 집을 잇는 경로가 딱 1개
    = 사이클이 없음
    = 트리구조
- 같은 서브트리 내의 경로는 통행료를 안냄
- 다르면 냄

- (첫번째 서브트리에 있는 노드) * (다른 서브트리에 포함된 노드) = 최댓값
- 간선을 하나씩 선택하여, 잘랐다고 가정하고, 그래프 탐색을 돌리면 된다.

- 그래프 탐색을 진행하면서, 자식의 노드 수를 더하게 되면, 그래프 탐색을 한번만 해도 된다.
'''

'''4번 로드밸런서
평균 8.65
-> 기술적인 지식 / 알고리즘 전혀 필요 없다

1. Round robin
뭐래 못봤음 ㅋㅋ 구현하기 쉽다는데?

2. least connection
요청이 들어올 때 이미 처리가 완료된 요청이 있을 수도 있다
새로운 요청이 들어오는 시간이랑 비교해서, 이미 들어온 요청이 끝났으면 데이터를 제거
deque를 쓰면 된다
'''

'''5번 kyul
평균 15.8
- 일부 숫자를 선택해서, 각 경우가 오름/내림차순인지 확인하면 됨
- 백트래킹 / 비트마스킹? 

- 오름차순으로 만들기 위해 지워야 하는 수 = 배열 전체의 길이 - 가장 긴 증가하는 부분 수열의 길이
- LIS를 구해서 배열 전체 길이에서 빼라
- 오름/내림차순 가능성 2개니까 2번 해라
'''

'''6번 마스크
평균 2.67
- 젤 어려웠단다
- 짜잘한 날짜 조정

- 윤년이 존재 안하니까, 날짜 관련 라이브러리 쓸 수 없었음
- 직접 문자열 파싱해서 년도 등등 구분해야했음

- 같은 날의 다른 가격 마스크 -> 가장 저렴한것만 남긴다

- with DP
- dp[x] x번째 날 부터 시작, 모든 날짜를 만족해서 마스크를 남길 .. 어쩌구
- x번째 날에,
    - 주어진 마스크 중 하나 구매 -> 날짜 비용 추가
    - 마스크 구매 안함(x날에 마스크를 안써도 되는)
    - 점화식 세워서 DP로 해결
'''
