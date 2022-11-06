'''실전 3 성적이 낮은 순서대로 학생 출력하기

## time = 5/20m

## info

## Logic
- 입력값은 string int로 들어온다
- 이걸 (이름 점수) 형태의 튜플로 받아서 list에 넣고
- settingFunc를 만들어서
- sort(array, setting = settingFunc)로 정렬
- 이름만 프린트
'''

n = int(input())
array = []
for i in range(n):
    tmp = input().split()
    array.append( (tmp[0], int(tmp[1])))

def settingFunc(array):
    return array[1]

array = sorted(array, key=settingFunc)

for i in array:
    print(i[0], end=' ')


## 답지 - 람다식 사용
array = sorted(array, key=lambda array:array[1])