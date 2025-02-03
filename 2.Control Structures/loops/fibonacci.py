#Write a Python program to print the Fibonacci series up to n terms, where n is entered by the user.

n= int(input("Enter the number : "))

a, b =0, 1
print("Fibonacci series :")

for i in range (n):
    print(a, end=" ")
    a, b = b, a+b
    