n = int(input())
answer = ''
for i in range(1, n+1):
    if '3' in list(str(i)) : answer += 'X '
    elif '6' in list(str(i)) : answer += 'X '
    elif '9' in list(str(i)) : answer += 'X '
    else: answer += str(i)+' '
print(answer)