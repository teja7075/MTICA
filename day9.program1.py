##def printSeriesIncreasing(ch,n):
##    assert isinstance(ch,str), "first argument should be string"
##    assert isinstance(n,int), 'seconsd argument should be int'
##    for i in range(1,n+1,1):
##        print(ch*i)
##    return None
def printSeriesDecreasing(ch,n):
    for i in range(n,0,-1):
        print(ch*i)
    return None


inpCh=input("enter a character:")
inpNum=int(input("enter a no:"))
##try:
##    printSeriesIncreasing(inpCh,inpNum)
##except AssertionError as ob:
##    print(ob)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
