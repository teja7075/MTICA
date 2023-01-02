sample_Dict={
            "name":"lucky",
            "Age":22,
            "salary":8000,
            "city":"banaglore"}
keys=["name","salary"]
d=dict()
for i in sample_Dict.keys()-keys:
    d[i]=sample_Dict[i]
print(d)


