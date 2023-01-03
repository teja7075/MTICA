class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,rollno):
        self.rollno=rollno
        self.name=name
    def displayStudent(self):
        print('name: '+self.name+'\nRollno: '+str(self.rollno))
        print('college: '+self.college+'\ncourse: '+self.course)
for i in range(2):
    n=input()
    r=int(input())
    obj=Student(n,r)
    obj.displayStudent()
    
              

              
              
        
