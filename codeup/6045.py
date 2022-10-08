a, b, c = map(int, input().split()) 
sum_ = a+b+c
avg_ = round(sum_/3, 2)
print(str(sum_) + " " + str(format(avg_, ".2f")))