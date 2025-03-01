
f = open("e:/python/5. File Input Output/demo.txt", "r")
data =f.read()
print(data)
print(type(data))
f.close()

line1=f.readline()
print(line1)