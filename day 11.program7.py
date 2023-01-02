sample_Dict={
            "name":"lucky",
            "Age":22,
            "salary":8000,
            "city":"banaglore"}
keys=["name","salary"]
newDict={}
for i in keys:
    newDict[i]=sample_Dict[i]
print(newDict)
newDict={i:sample_Dict[i] for i in keys }
print(newDict)

