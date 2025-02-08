#11.	Write a program to print a diamond pattern using loops:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *


rows = int(input("Enter the number of rows for the upper half: "))

# Upper part of the diamond
for i in range(1, rows + 1, 2):
    print(" " * ((rows - i) // 2) + "*" * i)

# Lower part of the diamond
for i in range(rows - 2, 0, -2):
    print(" " * ((rows - i) // 2) + "*" * i)
