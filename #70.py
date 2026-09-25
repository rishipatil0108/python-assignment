#70--Count consonants
str1="goodmorning"
counter=0
for i in str1:
    if i!='a' and i!='e' and i!='i' and i!='o' and i!='u':
        print(i,end=" ")
        counter+=1
print(counter)        