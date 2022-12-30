num1=input("enter a number:")
num2=input("enter a number:")

try:
    res=int(num1)/int(num2)
except ZeroDivisionError:
    print("exception handled by tej")
except ValueError:
    print("exception handled by lucky")
except  Exception as ob:
    print(ob)

##     print("division by zero not allowed")
else:
    print (num1, '/' ,num2, '=', res)
finally:
    print('thanks')
                 
print("visit again at python class at MTICA")
