#35--Find largest number from 1–N
n = int(input("How many numbers? "))
largest = int(input("Enter number 1: "))

for i in range(2, n+1):
    num = int(input(f"Enter number {i}: "))
    if num > largest:
        largest = num

print("Largest number:", largest)