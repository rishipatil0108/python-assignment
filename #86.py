#86
n = int(input("enter num "))
temp = n
sum=0
rem=0
length=len(str(temp))
while n!=0:
    rem=n%10
    sum+=rem
    n//=10
print(sum)    