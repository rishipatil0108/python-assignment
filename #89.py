#89
from math import factorial 
n =int(input("enter num "))
temp=n
rem=0
sum1=0
while n!=0:
    rem=n%10
    n//=10
    sum1+=factorial(rem)
if temp==sum1:
    print("strong")
else :
     print("not strong")    