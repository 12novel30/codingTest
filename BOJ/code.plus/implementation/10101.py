angle = []
ifEquilateral = True
ifIsoceles = False
for i in range(3):
    tmpAngle = int(input())
    
    if tmpAngle in angle:
        ifIsoceles = True
        
    angle.append(tmpAngle)
    
    if tmpAngle != 60:
        ifEquilateral = False

if ifEquilateral == True:
    print("Equilateral")
else:
    if sum(angle) != 180:
        print("Error")
    else:
        if ifIsoceles == True:
            print("Isosceles")
        else:
            print("Scalene")
