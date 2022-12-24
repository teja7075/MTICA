inpArea=int(input("Enter area of circle:"))
if inpArea<0:
    print('Invalid Area')
else:
    pi=3.14159
    radius=round((inpArea/pi)**(1/2),6)
    print("For the given Area",inpArea,"radius is:",radius)
    print("Area:"+str(inpArea),"radius:"+str(radius))
