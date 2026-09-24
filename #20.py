#20--Grade calculator from marks
n = int(input("enter marks(out of 100) "))
if n//10==10 or n//10==9:
    print("A")
elif n//10==8:
    print('B')  
elif n//10==7:
    print('C')
elif n//10==6:
    print('D')   
elif n//10==5:
    print('E')       
else:
    print("F")    