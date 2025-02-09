#Write a program to print a half pyramid pattern using numbers:
#1
#12
#123
#1234
#12345

n=int(input("Enter the number : "))

i=0

for i in range(1,n+1):
    for j in range(1,i+1):
        if i<=n:
            print(j,end=" ")
    print()
print(f'end with {n}')


"""rows = 5  

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print() 
"""