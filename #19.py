#19--Simple calculator using  if/elif
a = int(input("enter num1 "))
b = int(input("enter num2 "))
c = input("enter operand(+,-,*,/) ")
if c=='+':
    print("num1+num2= ",a+b)
elif c=='-':
    print("num1-num2= ",a-b)  
elif c=='*':
    print("num1xnum2= ",a*b)
elif c=='/':
    print("num1/num2= ",a/b)          
else:
    print("invalid syntax")    