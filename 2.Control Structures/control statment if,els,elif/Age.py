#Write a program that asks for a user’s age and checks whether they are eligible to vote (age ≥ 18).

age= int(input("Enter the age :"))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")