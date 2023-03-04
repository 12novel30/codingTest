def solution(record):
    answer = []
    d = {}
    for r in record:
        tmp = r.split()
        if tmp[0] == "Enter":
            d[tmp[1]] = tmp[2]
            answer.append([tmp[1], "님이 들어왔습니다."])
        elif tmp[0] == "Leave":
            answer.append([tmp[1], "님이 나갔습니다."])
        elif tmp[0] == "Change":
            d[tmp[1]] = tmp[2]
    final = []
    for message in answer:
        final.append(d[message[0]]+message[1])
    
    return final