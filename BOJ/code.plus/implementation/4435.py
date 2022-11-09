ganType = [1,2,3,3,4,10]
sauType = [1,2,2,2,3,5,10]

battleCount = int(input())
resultBattle = []

def listCross(typelist, countlist):
    sum = 0
    for i in range(len(typelist)):
        sum += typelist[i] * countlist[i]
    return sum

for i in range(battleCount):
    
    ganCount = list(map(int, input().split()))
    sauCount = list(map(int, input().split()))
    if listCross(ganType, ganCount) > listCross(sauType, sauCount):
        resultBattle.append("Good triumphs over Evil")
    elif listCross(ganType, ganCount) < listCross(sauType, sauCount):
        resultBattle.append("Evil eradicates all trace of Good")
    else:
        resultBattle.append("No victor on this battle field")

for i in range(battleCount):
    print("Battle " + str(i+1) + ": " + resultBattle[i])