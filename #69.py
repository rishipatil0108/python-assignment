#69--Count vowels
str1="goodmorning"
counter=0
for i in str1:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        print(i,end=" ")
        counter+=1
print(counter)        