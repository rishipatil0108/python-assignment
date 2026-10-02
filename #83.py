#83--armstrong number
n= int(input("enter num "))
temp=n
length=len(str(temp))
sum=0
while n!=0:
    rem=n%10
    sum+=rem**length
    n=n//10
    
if sum==temp:
    print("armstrong number")
else:
    print("not armstrong")    