class Circle:
    pi=22/7
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        temp=self.pi*self.radius**2
        return temp
    def perimeter(self):
        temp= 2*self.pi*self.radius
        return temp
    
r=int(input())
obj=Circle(r)
area=obj.Area()
peri=obj.perimeter()
print('area of circle with radius',r,'is',area)
print('perimeter of circle with radius',r,'is',peri)
