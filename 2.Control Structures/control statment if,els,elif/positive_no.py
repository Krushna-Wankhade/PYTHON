#Write a Python program to check if a given number is positive, negative, or zero.

n= int(input("Enter the number: "))

if n > 0:
    print(f"{n} is a positive number.")
elif n < 0:
    print(f"{n} is a negative number.")
else:
    print(f"{n} is a zero.")
    