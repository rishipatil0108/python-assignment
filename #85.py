#85
n = int(input("enter num "))
temp = n
rev=0
rem=0
length=len(str(temp))
while n!=0:
    rem=n%10
    rev+=rem*10**(length-1)
    n//=10
    length-=1
print(rev)    