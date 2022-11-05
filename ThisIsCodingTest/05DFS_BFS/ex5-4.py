def recursive(i):
    if i<=10:
        print("재귀~ in " + str(i) + "step")
        i += 1
        recursive(i)
    else: return
    

recursive(1)