# "w" for writing and truncate the file first

f = open("e:/python/5. File Input Output/demo.txt", "w")

f.write("I want to learn the advance python.")

f.close()

# "a" for writing,appending to the end of the line file fi it exist

f = open("e:/python/5. File Input Output/demo.txt", "a")

f.write("Then i'll move to the java")

f.write("\n After that c++")

f.close()


f= open("e:/python/5. File Input Output/sample.txt", "w")
f.close