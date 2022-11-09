#5/15
# global sumBox
# global countBox
# global minBBang
# global maxBBang
# global namuge
# sumBox, countBox, minBBang, maxBBang, namuge = 0,0,0,0,0

# def reBBang(box):
#     global sumBox
#     global countBox
#     global minBBang
#     global maxBBang
#     global namuge
#     sumBox = sum(box)
#     countBox = len(box)
#     minBBang = sumBox//countBox
#     if sumBox%countBox==0:
#         maxBBang = minBBang
#     else:
#         maxBBang = minBBang + 1
#     namuge = countBox - sumBox%countBox
#     print(sumBox, countBox, minBBang, maxBBang, namuge)

# def solution(box):
#     # Write your code here
#     global sumBox
#     global countBox
#     global minBBang
#     global maxBBang
#     global namuge
    
#     answer = 0
#     reBBang(box)
#     print(box)
#     for i in range(len(box)-1, 0, -1):
        
#         if namuge != 0:
#             standard = minBBang
#             namuge -= 1
#         else:
#             standard = maxBBang
        
#         if box[i] < standard:
#             reBBang(box[:i])
#         elif box[i] == standard:
#             continue
#         else:
#             box[i] = standard
#             box[i-1] += box[i] - standard

#     print(box)
#     answer = max(box)
#     return answer