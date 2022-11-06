'''실전 4 두 배열의 원소 교체

## time = 12m/20m

## info
1. 두개의 배열 a b
2. 목표: a의 합이 최대
3. a <-> b 를 k번 할 수 있음
4. 출력: a의 합

## Logic
- a의 min <-> b의 max를 k번
- 그냥 양쪽을 소팅하는게 낫나?
- 양쪽을 소팅해서, 그 중 옮길 녀석들을 정하고 시작하는게 나을듯
- 근데 a의 min이 b의 max보다 크게 될 수도 있으니까, 그 전에 멈추기
- => 그냥 옮길 녀석들을 안정하고 일일이 비교해도 됨
'''

n,k = map(int, input().split())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

lista.sort()
listb.sort(reverse=True)

index = k-1
for i in range(k):
    if lista[index] <= listb[index]: break
    else:
        index -= 1

summ = sum(listb[0:index+1]) + sum(lista[index+1:])
print(summ)

## 아래는 답지 풀이
for i in range(k):
    if lista[i] < listb[i]:
        lista[i], listb[i] = listb[i], lista[i]
    else: break
