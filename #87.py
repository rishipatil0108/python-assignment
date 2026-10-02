#87
n = int(input("enter num "))
count=0
while n!=0:
    count+=1
    n//=10
print(count)