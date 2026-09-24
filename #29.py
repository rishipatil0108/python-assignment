#29--Find factorial of N
n = int(input("enter num "))
a=1
for i in range(n,1,-1):
    a*=i
print(a)