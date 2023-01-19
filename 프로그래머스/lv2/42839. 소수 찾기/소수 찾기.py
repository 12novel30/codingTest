from itertools import permutations

def solution(numbers):
    numP = createPermutation(list(numbers))
    return checkIsPrime(numP)

def createPermutation(numList):
    numP = []
    for i in range(len(numList)):
        numP += permutations(numList,i+1)
    return numP

def checkIsPrime(numbers):
    answer = 0
    tmpNumberList = []
    primeList = []
    for strN in numbers:
        isNotPrime = False
        n = ''.join(s for s in strN)
        intN = int(n)
        if intN not in tmpNumberList:
            tmpNumberList.append(intN)
            if len(n) == 1:
                if intN == 2 or intN == 3 or intN == 5 or intN == 7:
                    primeList.append(intN)
                    answer += 1
            else:
                if int(n[-1])%2 == 0: continue
                
                for i in range(3, int(intN**(1/2))+1):
                    if i%2 == 0: continue
                    if intN%i == 0:
                        isNotPrime = True
                        break
                
                if isNotPrime == False:
                    primeList.append(intN)
                    answer += 1
    return answer