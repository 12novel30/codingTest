def solution(box):
    # Write your code here
    answer = 0
    
    if sum(box)%len(box)==0:
        standard = sum(box)//len(box)
        extra = -1
    else:
        standard = sum(box)//len(box) + 1
        extra = len(box) - sum(box)%len(box)
    
    minBox = box.index(min(box))
    maxBox = box.index(max(box))
    while minBox < maxBox and box[minBox] < standard:
        print(box)
        print(1)
        if box[maxBox] > standard:
            box[minBox] = standard
            box[maxBox] -= standard - box[minBox]
            print(box)
            if extra > 0:
                extra -= 0
            elif extra == 0:
                extra = -1
                standard -= 1
            else: 
                extra = -1
            
            minBox = box.index(min(box))
            maxBox = box.index(max(box))
        print(box)
        print(2)
    print(box)
    print(3)

    return max(box)