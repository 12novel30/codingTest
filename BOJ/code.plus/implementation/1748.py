n = input()
digit = len(n)
n = int(n)

'''
n = 1~9
-> 1*n

n = 10~99
-> 2*(n-9) + 1*9

n = 100~999
-> 3*(n-99) + 2*(90) + 1*9

digit = len(n)
=> digit*(n - (10**(digit-1) - 1)) + (digit-1)*(10**(digit-2)*9) + (digit-2)*(10**(digit-3)*9)

n=1-9
digit = 1
1*(n - (10**0-1)) = 1*n
0*

'''

result = digit*(n - (10**(digit-1) - 1))

while digit > 0:
    digit -= 1
    result += digit*(10**(digit-1)*9)

print(int(result))
