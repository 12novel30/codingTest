# 코테 준비중
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i,p in enumerate(prices):
        if i == 0:
            stack.append([p,i])
        else:
            while stack[-1][0] > p:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
                if len(stack) == 0: break
            stack.append([p,i])
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(answer)-1 - i
    return answer