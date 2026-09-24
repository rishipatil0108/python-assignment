#37--Count numbers divisible by 3
n = int(input("enter num "))
for i in range(1,n+1):
    if i%3==0:
        print(i, end=" ")