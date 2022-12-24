def checkEven(n):
    if n<0:
        return "INVALID"
    n=str(n)
    if(n[-1]=='0' or n[-1]=='2' or n[-1]=='4' or n[-1]=='6' or n[-1]=='8'):
        return "EVEN"
    if(n[-1]=='1' or n[-1]=='3' or n[-1]=='5' or n[-1]=='7' or n[-1]=='9'):
        return "ODD"
inpNum=int(input())
print(checkEven(inpNum))
    
