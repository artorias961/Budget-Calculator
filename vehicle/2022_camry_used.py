"""
Christopher Morales

Paying the principal vs not paying the principal
"""
import numpy_financial as npf
import pandas as pd

# Function to calculate loan details without extra payments
def loan_schedule(principal, annual_rate, years, extra_payment=0):
    monthly_rate = annual_rate / 12
    n_payments = years * 12
    monthly_payment = npf.pmt(monthly_rate, n_payments, -principal)
    
    balance = principal
    schedule = []

    for i in range(1, n_payments + 1):
        interest = balance * monthly_rate
        principal_payment = monthly_payment - interest
        if extra_payment > 0:
            principal_payment += extra_payment
        balance -= principal_payment
        
        schedule.append({
            'Month': i,
            'Payment': monthly_payment + extra_payment,
            'Principal Payment': principal_payment,
            'Interest Payment': interest,
            'Remaining Balance': balance
        })
        
        if balance <= 0:
            break

    return pd.DataFrame(schedule)

# Boolean statement to create CSV file
create_csv_file = False

# Parameters
principal = 32000  # Loan amount
annual_rate = 0.05  # Annual interest rate
years = 5  # Loan term in years
extra_payment = 500  # Extra monthly payment towards principal

# Calculate schedules
schedule_without_extra = loan_schedule(principal, annual_rate, years)
schedule_with_extra = loan_schedule(principal, annual_rate, years, extra_payment)

# If true then create the CSV
if create_csv_file:
    # Save to CSV files
    schedule_without_extra.to_csv('Loan_Schedule_Without_Extra_Payments.csv', index=False)
    schedule_with_extra.to_csv('Loan_Schedule_With_Extra_Payments.csv', index=False)

# Display the first few rows of the dataframes
print("Loan Schedule Without Extra Payments")
print(schedule_without_extra.head())

print("\nLoan Schedule With Extra Payments")
print(schedule_with_extra.head())
