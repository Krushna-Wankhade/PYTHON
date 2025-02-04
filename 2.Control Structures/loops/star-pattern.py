#	Write a Python program to print a pattern of stars like this:
#markdown
#CopyEdit
#*
#**
#***
#****
#*****
n=int(input("Enter the numbe: "))
i=0

for i in range(1,n+1):
    if i<=n:
        print('*'*i)
        i+=1
        
        
    
