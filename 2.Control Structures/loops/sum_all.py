#4.	Write a Python program to calculate the sum of all numbers from 1 to n, where n is entered by the user.

n=int(input("Enter the number : "))

i=0

while range (i,n+1):
    i=n*(n+1)//2
    
print(f"The sum of the all number from 1 to {n} is {i}")