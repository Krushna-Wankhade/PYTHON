#Write a Python program to determine the largest of three numbers entered by the user.

A= int(input("Enter the first no. :"))
B= int(input("Enter the second no. :"))
C= int(input("Enter the third no. :"))

if A > B:
    print(f"{A} is largest.")
elif B > C:
    print(f"{B} is largest.")
elif C > B:
    print(f"{C} is largest.")
