def fun(str1):
    print(str1)
    return
fun("i'm first call to user defined function!")
fun(" Again second call to the same function")

def printtme(str1,n):
    n[0]='lucky'
    print (str1,n)
    return
x=['tej','lucky']
printtme("wakeup",x)
print('x:',x)

def changeMe(lstn):
    lstn=['lucky','tej','kulle']
    print(lstn)
lst=[2,34,22,55]
print(changeMe(lst))
