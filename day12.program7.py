class Number:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mult(self):
        return self.n1*self.n2
    def div(self):
        return self.n1/self.n2
n1=int(input())
n2=int(input())
ob=Number(n1,n2)
try:
    print(n1,'/',n2,'=',ob.div(),sep='')
except ZeroDivisionError as obj:
    print(obj)
print(n1,'-',n2,'=',ob.sub(),sep='')
print(n1,'+',n2,'=',ob.add(),sep='')
print(n1,'*',n2,'=',ob.mult(),sep='')

