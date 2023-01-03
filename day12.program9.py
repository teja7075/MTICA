class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0), "INVALID"
        self.length=length
        self.width=width
    def Area(self):
        temp=self.length*self.width
        return temp
    def perimeter(self):
        temp=(self.length+self. width)*2
        return temp
    
r=int(input())
s=int(input())
try:
    ob=Rectangle(r,s)
    area=ob.Area()
    peri=ob.perimeter()
    print('area of Rectangle with radius',r,'is',area)
    print('perimeter of Rectangle with radius',r,'is',peri)
except AssertionError as ob:
    print(ob)
