def factorial_iterative(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    return result

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)
    
print("반복 iterative " + str(factorial_iterative(5)))
print("재귀 recursive " + str(factorial_recursive(5)))