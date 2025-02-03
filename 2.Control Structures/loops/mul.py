#Write a program that asks the user to enter a number and prints the multiplication table for that number
# (e.g., for 5, it prints 5 × 1, 5 × 2, ... up to 5 × 10).

n=int(input("Enter the number : "))

i=1

while i<=10:
    print(i*n)
    i+=1