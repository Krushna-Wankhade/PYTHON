#Write a Python program to calculate the electricity bill. The charges are as follows:
#For the first 100 units: ₹5 per unit
#For the next 100 units: ₹7 per unit
#For units above 200: ₹10 per unit


Unit=int(input("Enter the unit consumed :"))

if Unit < 0:
        print("Units consumed cannot be negative. Please enter a valid value.")
elif Unit <=100:
    print(f"The total electricity bill for {Unit} units is",f"{Unit*5} ₹")
elif 100 <= Unit <=200:
    print(f"The total electricity bill for {Unit} units is",f"{Unit*7} ₹")
elif Unit >= 200:
    print(f"The total electricity bill for {Unit} units is",f"{Unit*10} ₹")