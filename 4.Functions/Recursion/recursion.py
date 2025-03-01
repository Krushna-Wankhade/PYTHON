#Recursion in Python refers to a function calling
# itself to solve smaller instances of the same problem until it reaches a base condition.

#recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    
show(5)