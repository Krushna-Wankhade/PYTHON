s=input("enter: ")
v=["a,e,i,o,u,A,E,I,O,U"]
c=0

for p in s:
    if(s.count(p) == 1):
        c=c+1
print(c)