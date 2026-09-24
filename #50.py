#50--Number pyramid
for i in range(1,11):
    print(" " * (10-i), end="")
    for j in range(1,i+1):
        print(j, end=" ")
    print()    