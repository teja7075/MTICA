def sumDigit(n):
    n=str(n)
    total=0
    for i in n:
        total +=int(i)
    return total

n=int(input("Enter a number:"))
count=len(str(sumDigit(n)))
while(count!=1):
    n=sumDigit(n)
    count=len(str(sumDigit(n)))
print(n)
             
