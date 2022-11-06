specs = [["A", 10, 3], ["B", 20, 4], ["C", 15, 5]]

'''
a-b
b-c
c-a
이렇게 경기를 하게 되어있음. - 어차피 모두랑 경기함

a가 이긴 사람을 담을 리스트?

'''
def solution(specs):
    score = []
    winPerson = []
    
    # 이긴 경우의 수 나열 ...
    for i in range(len(specs)):
        tmpWinPerson = []
        first = specs[i]
        score.append([first[0], 0, tmpWinPerson])
        for j in range(len(specs)):
            second = specs[j]
            # 서로 다른 선수들이 경기할 때
            if first[0] != second[0]:
                iScore = first[1] + second[1]*first[2]
                jScore = second[1] + first[1]*second[2]
                if iScore > jScore: 
                    score[i][1] += 1
                    score[i][2].append(second[0])
    
    answerScore = sorted(score, key=lambda val:val[1], reverse=True)
                               
    # 본인이 이긴 경기의 수만큼은 어차피 줘야 함
    # 자기보다 앞에 자기가 이긴 사람이 없도록 해야하는데 ...
    answer = [answerScore[0][0]] + answerScore[0][2]
    for s in answerScore:
        if s[0] not in answer:
            answer = [s[0]] + answer
        tmp = []
        for t in s[2]:
            if t not in answer:
                tmp.append(t)
        answer = answer + tmp
                    
    
    return answer

print(solution(specs))