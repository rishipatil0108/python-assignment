#15--Find greatest of three numbers
a = int(input("enter num1 "))
b = int(input("enter num2 "))
c = int(input("enter num3 "))
if a>b and a>c:
    print("num1 is greatest")
elif b>c and b>a:
    print("num2 is greatest")    
else:
    print("num3 is greatest")    