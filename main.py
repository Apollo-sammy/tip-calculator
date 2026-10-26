# Tip Calculator
# This program calculates a tip and the total bill.

try:
    bill = float(input("Enter the bill amount: KSh "))
    tip_percentage = float(input("Enter the tip percentage: "))

    if bill < 0 or tip_percentage < 0:
        print("Please enter amounts that are not negative.")
    else:
        tip = bill * tip_percentage / 100
        total = bill + tip

        print(f"\nTip: KSh {tip:.2f}")
        print(f"Total bill: KSh {total:.2f}")

except ValueError:
    print("Please enter numbers only. Try again.")
