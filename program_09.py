import function_08
start=int(input())
stop=int(input())
lst=[]
for i in range(start,stop+1):
    if function_08.checkPrimeNumber(i):
        lst.append(i)
print(*lst)
print(len(lst))
