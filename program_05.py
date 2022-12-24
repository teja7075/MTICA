import function_04
lst=[]
for i in range(100,1000):
    if function_04.checkArmstrongNumber(i):
        lst.append(i)
print(lst)
