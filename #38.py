#38--Print factors of a number
n = int(input("enter num "))
for i in range(1,n+1):
    if n%i==0:
        print(i, end=" ")