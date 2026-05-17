principal = float(input("Enter the loan amount: "))
rate = float(input("Enter the annual interest rate: "))
tenure_months = int(input("Enter the tenure in months: "))
years = tenure_months / 12 
print("Select compounding frequency: ")
print("1. Yearly \n 2. Half-Yearly \n 3.Quarterly \n 4. Monthly \n 5. Daily ")
choice = int(input("Enter the compounding frequency (1-5): "))
n = "How many times per year interest is compounded"
if choice == 1: 
     print("Compounding frequency: Yearly")
     n = 1
elif choice == 2:
    print("Compounding frequency: Half-Yearly")
    n = 2
elif choice == 3:
    print("Compounding frequency: Quarterly")
    n = 4
elif choice == 4:
    print("Compounding frequency: Monthly")
    n = 12
elif choice == 5:
    print("Compounding frequency: Daily")
    n = 365
else:
    print("Invalid choice. Defaulting to yearly compounding.")
    n = 1
final_amount = principal * (1 + rate/n) ** (n * years)
total_interest = final_amount - principal
total_repayment = principal + total_interest
monthly_emi = (principal * rate * (1 + rate) ** tenure_months) / ((1 + rate) ** tenure_months - 1)
if principal > 0 and rate >= 0 and rate <= 50 and years > 0:
    #proceed with the calculations\
    print("The loan amount is : rupees", principal)
    print("The interest rate is :  % per year", rate)
    print("The tenure is : years", years)
    print("The total interest is : rupees", total_interest)
    print("The total repayment is : rupees", total_repayment)
    print("The monthly EMI is : rupees", monthly_emi)
else:
    print("Invalid input. Please check the values entered.") 
monthly_income = int(input("Enter your monthly income: "))
if monthly_emi > monthly_income * 0.5:
    print("The EMI is too high compared to your monthly income. Consider reducing the loan amount or increasing the tenure.")
else:
    print("The EMI is manageable compared to your monthly income.")
def amortization_schedule(principal, rate, tenure_months, n):
    starting_balance = principal 
    monthly_interest_rate = rate / 12 / 100
    print(f"{'Month':<8} {'EMI':<12} {'Interest':<12} {'Principal':<12} {'Balance':<12}")
    for month in range(1, tenure_months + 1):
        current_balance = starting_balance
        interest_payment = current_balance * monthly_interest_rate
        principal_payment = monthly_emi - interest_payment
        starting_balance -= principal_payment
        print(f"{month:<8} {monthly_emi:<12.2f} {interest_payment:<12.2f} {principal_payment:<12.2f} {starting_balance:<12.2f}")
print("\nAmortization Schedule:")
# === ADD THIS CODE AFTER YOUR AMORTIZATION SCHEDULE LOOP ===

import json
from datetime import datetime

# Calculate totals
total_paid = emi * tenure_months
total_interest = total_paid - principal

# Display summary
print("\n" + "="*50)
print("LOAN SUMMARY")
print("="*50)
print(f"Monthly EMI: ₹{emi:.2f}")
print(f"Total Amount Paid: ₹{total_paid:.2f}")
print(f"Total Interest Paid: ₹{total_interest:.2f}")
print(f"Principal: ₹{principal:.2f}")
print("="*50)

# Ask user if they want to save
save = input("\nDo you want to save this scenario? (yes/no): ").strip().lower()

if save == 'yes':
    # Get scenario name
    name = input("Enter a name for this scenario: ").strip()
    
    # Create scenario dictionary
    scenario = {
        "name": name,
        "saved_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "principal": principal,
        "annual_rate": annual_rate,
        "tenure_months": tenure_months,
        "monthly_emi": round(emi, 2),
        "total_interest": round(total_interest, 2),
        "total_paid": round(total_paid, 2)
    }
    
    # Load existing file or create new
    try:
        with open("loan_scenarios.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"scenarios": []}
    
    # Add new scenario
    data["scenarios"].append(scenario)
    
    # Save to file
    with open("loan_scenarios.json", "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"\n✅ Scenario '{name}' saved successfully!")
    print("📁 File: loan_scenarios.json")
else:
    print("\nScenario not saved.")

