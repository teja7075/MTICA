fo=open(r"D:\python practices62\day9\tej.txt","r")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inspstr+'\n')
fo.close()
print("written to file")
