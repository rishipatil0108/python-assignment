#61--Search for an element
list1=[1,2,3,4,5]
n = int(input("search element "))
found=False
for ele in list1:
    if ele==n:
        found=True    
        break
if found==True:
        print("found",ele)
else:
        print("not found")            