rev=0
n=789
while(n):
    rev=rev*10+n%10
    n=n//10
print(rev)
