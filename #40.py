#40--Print prime numbers from 1–N
n = int(input("enter num "))
for i in range(2,n+1):
        prime=True
        for j in range(2,i):
                if i%j==0:
                        prime=False
        if prime==True:
                 print(i)