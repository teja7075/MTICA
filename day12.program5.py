class Dog:
    price=400
    def __init__(self,name,color):
        self.color=color
        self.name=name
    def bark(self):
        print("wolf")
        print(self.name, " has " ,self.price," price and its color is ",self.color)

if __name__=="__main__":
    pet1=Dog("tommy","brown")
    pet2=Dog("puppy","black")
    pet1.bark()
    pet2.bark()
    print(pet1.price)
    print(pet2.price)
    print(Dog.price)
    Dog('abc','blue').bark()
