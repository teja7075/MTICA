set1={10,20,30,40,50}
set2={70,80,90,10,60}
if set1.isdisjoint(set2):
    print("two sets have no items in common")
else:
    print("two sets have  items in common")
    print(set1.intersection(set2))
