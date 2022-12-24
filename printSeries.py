def printSeries(n):
    temp=[]
    for i in range(n+1):
        temp.append(i)
    return temp
a=int(input("Enter a number:"))
ans=printSeries(a)
print(*ans)
print(sum(ans))
 
