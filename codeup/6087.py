n = int(input())
a = 1
answer = ''
while a<=n:
    if a%3 != 0: answer += str(a)+' '
    a += 1
print(answer)