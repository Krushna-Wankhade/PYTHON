#6.	Write a program to find the factorial of a number using a for loop.

n= int(input("Entrer the number : "))

i=1

for p in range (1,n+1):
    i*=p
print(f"The factorial of {n} is {i}")   