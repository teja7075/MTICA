import math
inpArea=int(input("Enter area of Circle:"))
radius=round(math.sqrt(inpArea/math.pi),6)
print("For the given Area",inpArea,"radius is:",radius)
print("Area:"+str(inpArea),"radius:"+str(radius))
