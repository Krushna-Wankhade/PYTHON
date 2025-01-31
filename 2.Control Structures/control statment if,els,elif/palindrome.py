#Write a Python program that accepts a string input and checks whether it is a palindrome or not using an if-else statement.

string =input("Enter the string: ")

if string ==string[::-1]:
    print(f'"{string}" is a palindrome')
else:
    print(f'"{string}" is not a palindrome')