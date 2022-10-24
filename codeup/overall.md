# Overall; codeup
- how to get input value()
    - to int
        1. a = int(input())
    - to float
        1. a = float(input())
    - split
        1. a,b = map(int, input().split()) #default: space
    - format
        1. print(format(a, ".2f"))
- how to print specific string
    1. ' "Hello World" '
    2. 출력할 " -> " \"!@#$%^&*()' "
    3. 출력할 \ -> " \"C:\Download\\'hello'.py\" "
    4. 출력할 \n -> r'print("Hello\nWorld")'
    5. print 내에서 연산한 결과(true, false) 출력
        - print(a<b)
        - = if a<b: print(True)
        - = else: print(False)
- how to get another number
    1. 16, hex) print('%x'%int(a))
    2. 16, hex, capital) print('%X'%int(a))
    3. decimal to unicode) n = ord(input())
    4. int to char) chr(ord(input()))
- bit operation
    1. print(a<<1) # a*2
- etc
    - a^b) a**b