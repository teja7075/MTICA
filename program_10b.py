def checkEven(n):
    if n<0:
        return "INVALID"
    if inpNum%2==0:
        return "EVEN"
    return "ODD"
inpNum=int(input())
print(checkEven(inpNum))
