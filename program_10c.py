def checkEven(n):
    if n<0:
        return "INVALID"
    n=str(n)
    if n[-1] in '02468':
        return "EVEN"
    if n[-1] in '1357':
        return "ODD"
inpNum=int(input())
print(checkEven(inpNum))
    
