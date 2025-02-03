#5.	Write a Python program to reverse a given number using a while loop.
n=int(input("Enter the number : "))

p=0

while n > 0:
    i=n%10
    p=p*10+i
    n=n//10

print(f"The revrs number is {p}")
    
    
    