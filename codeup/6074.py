c = ord(input()) # char의 정수값 리턴
a = ord('a')
while a<=c:
    print(chr(a), end = ' ') # char의 정수버전 값 -> 다시 char로 리턴
    a+=1