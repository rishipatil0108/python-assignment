num1=int(input("enter num1 "))
num2=int(input("enter num2 "))

list1=[]
list2=[]
for i in range(1,num1+1):
    if num1%i==0:
        list1.append(i)

for j in range(1,num2+1):
    if num2%j==0:
        list2.append(j)        

list0=list(set(list1)&set(list2))

largest=0
for ele in list0:
    if largest<ele:
        largest=ele

lcm=(num1*num2)//largest
print("lcm=",lcm)