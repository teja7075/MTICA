fo1=open(r"D:\python practices62\day9\tej.txt","r")
fo2=open(r"D:\python practices62\day9\tej1.txt","w+")

temp=fo1.read()
fo2.write(temp)
fo1.close()
fo2.close()              
print("file copied")
