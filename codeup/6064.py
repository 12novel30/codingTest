a,b,c = map(int, input().split())
# 3항 연산
print((a if (a<b) else b) if ((a if (a<b) else b)<c) else c)