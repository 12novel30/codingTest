def solution(buildings):
    nak = ['n', 'a', 'k', 'n', 'a', 'k']
    plusnak = ['n', 'a', 'k']
    answer = []
    
    for building in buildings:
        
        for i in nak:
            index = building.find(i)
            if index == -1:
                break
            building = building[index:]
        
        if index == -1:
            answer.append("X")
        else:
            for i in plusnak:
                plusindex = building.find(i)
                if plusindex == -1:
                    break
                building = building[index:]
            if plusindex == -1:
                answer.append("O")
            else:
                answer.append("X")
    
    return answer

b = ["naknakn", "naknaknak", "nak","","i_am_not_a_kim_and_not_awk", "nananananakkkk"]
print(solution(b))