#8--Calculate total and percentage of 5 subjects
m = int(input("marks of maths"))
p = int(input("marks of physics"))
c = int(input("marks of chemistry"))
e = int(input("marks of english"))
b = int(input("marks of biology"))
total = m+p+c+e+b
perc = (total/500)*100
print(f"total marks= {total}")
print(f"percentage= {perc}")