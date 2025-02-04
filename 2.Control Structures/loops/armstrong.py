#Write a Python program to check if a number is an Armstrong number (e.g., 153 is an Armstrong number because 1³ + 5³ + 3³ = 153).


n=int(input("Enter the Number : "))

d= len(str(n))

i=0
t=n

while t>0:
    digit=t%10
    i+=digit ** d
    t //=10

if i == n:
    print(f"{n} is the Armstrong number.")
else:
    print(f"{n} is not Armstrong number.")