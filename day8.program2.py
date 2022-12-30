def Factorial(num):
    assert (num>=0), "factorial of numbers is not defined!"
    if num==0:
        return 1
    else:
        return num*Factorial (num-1)
try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)
try:
    print(Factorial(45))
except Exception as obj:
    print(obj)
