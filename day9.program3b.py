def printMonth(dn):
    mn=''
    if (dn==1):
        mn='january'
    elif (dn==2):
        mn='february'
    elif (dn==3):
        mn= 'march'
    elif (dn==4):
        mn=  'april'
    elif (dn==5):
        mn='may'
    elif (dn==6):
        mn='june'
    elif (dn==7):
        mn='july'
    elif (dn==8):
        mn='august'
    elif (dn==9):
        mn='september'
    elif (dn==10):
        mn='october'
    elif (dn==11):
        mn='november'
    elif (dn==12):
        mn='december' 
    return mn
def printMonth1(dn):
    mn=''
    if (dn==1):
        mn='january'
    elif (dn==2):
        mn='february'
    elif (dn==3):
        mn= 'march'
    elif (dn==4):
        mn=  'april'
    elif (dn==5):
        mn='may'
    elif (dn==6):
        mn='june'
    elif (dn==7):
        mn='july'
    elif (dn==8):
        mn='august'
    elif (dn==9):
        mn='september'
    elif (dn==10):
        mn='october'
    elif (dn==11):
        mn='november'
    elif (dn==12):
        mn='december'
    return mn
import time
for i in range(7):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print((time.time()-start)*10000000)
    start=time.time()
    print(printMonth1(inpNum))
    print((time.time()-start)*10000000)
    
