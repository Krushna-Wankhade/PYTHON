#Write a program to find the largest number in a list using a loop.

n=list(map(int,input("Enter the numbers : ").split()))

i=n[0]

for p in n:
    if p>i:
        i=p
print(f"The largest number in the list is {i}")    