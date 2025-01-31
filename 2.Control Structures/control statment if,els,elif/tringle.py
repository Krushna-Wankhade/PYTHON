#Write a program to determine whether a given triangle is valid or not based on the three side lengths entered by the user.

s1 = int(input("Enter the value of first side :"))
s2 = int(input("Enter the value of second side :"))
s3 = int(input("Enter the value of third side :"))

if (s1+s2 > s3) and (s2+s3 > s1) and (s1+s3 > s2):
    print("The trangle is valid.")
else:
    print("The trangle is not valid.")