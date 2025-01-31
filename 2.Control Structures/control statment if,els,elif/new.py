def calculate_electricity_bill(units):
    # Initialize the total bill amount
    bill = 0

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        # First 100 units at ₹5 per unit
        bill = 100 * 5
        # Remaining units (units - 100) at ₹7 per unit
        bill += (units - 100) * 7
    else:
        # First 100 units at ₹5 per unit
        bill = 100 * 5
        # Next 100 units at ₹7 per unit
        bill += 100 * 7
        # Remaining units (units - 200) at ₹10 per unit
        bill += (units - 200) * 10

    return bill


# Input: number of units consumed
try:
    units_consumed = int(input("Enter the number of units consumed: "))
    if units_consumed < 0:
        print("Units consumed cannot be negative. Please enter a valid value.")
    else:
        # Calculate and display the bill amount
        bill_amount = calculate_electricity_bill(units_consumed)
        print(f"The total electricity bill for {units_consumed} units is ₹{bill_amount:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
