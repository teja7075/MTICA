class Number:
    def __init__(self,n):
        self.n=n
    def checkEven(self):
        if self.num%2==0:
            return 'even'
        else:
            return 'odd'
inp=int(input())
obj=Number(inp)
print(inp,"is",obj.checkEven())
