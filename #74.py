#74
n = input("enter string")
m = input("which char to search?")
c=0
for i in n:
    if m==i:
        c+=1
print(m,"occured",c,"times")
print(m,"occured",n.count(m),"times")