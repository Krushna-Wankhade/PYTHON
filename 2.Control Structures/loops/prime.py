#Write a program to print all prime numbers between 1 and 100 using a loop.

print("Prime number between 1 and 100 are : ")

for n in range(1,101):
    if n<2:
        continue
    
    prime=True
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            prime=False
            break
        
    if prime:
        print(n,end=" ")

