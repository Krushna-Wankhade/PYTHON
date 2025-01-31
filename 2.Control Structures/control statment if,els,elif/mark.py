# Write a program to take the user's marks and determine their grade based on the following:
#Marks ≥ 90: Grade A
#Marks 80–89: Grade B
#Marks 70–79: Grade C
#Marks 60–69: Grade D
#Marks < 60: Fail

Marks= int(input("Enter marks : "))

if Marks >= 90:
    print("Grade A ")
elif 80<= Marks <=89:
    print("Grade B")
elif 70<= Marks <=79:
    print("Grade C")
elif 60<= Marks <=69:
    print("Grade D")
elif Marks < 60 :
    print("Fail")

