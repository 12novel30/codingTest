h, b, c, s = map(int, input().split())
answer = h*b*c*s/8/1024/1024
print(format(answer,".1f")+ " MB")