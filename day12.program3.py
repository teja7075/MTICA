set1={10,20,30,40,50,90}
set2={30,40,70,80,90,60,}
#print(set1.intersection(set2))
#print(set1.union(set2))
#print(set1^set2) //remove duplicates
#set1.difference_update(set2)
#print(set1)
#print(set1.symmetric_difference(set2))//s2-s1unions1-s2
##set1.symmetric_difference_update(set2)
##print(set1)
set1.intersection_update(set2)
print(set1)

