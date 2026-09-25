#73--Check whether a string is palindrome
str1=input("enter string")
a = str1[::-1]
if str1==a:
    print("palindrome")
else:
    print("not palindrome")    
print(a)