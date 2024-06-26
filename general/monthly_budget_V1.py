import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class MonthlyNetIncome:
    def __init__(self, gross_annual_salary, federal_tax_brackets, state_tax_brackets, local_tax_rate, fica_rate, medicare_annual_cost, retirement_contribution_annual, savings_rate, car_insurance_annual_cost):
        """
        Initialize the MonthlyNetIncome with necessary parameters.

        :param gross_annual_salary: Annual salary before deductions
        :param federal_tax_brackets: List of tuples for federal tax brackets (limit, rate)
        :param state_tax_brackets: List of tuples for state tax brackets (limit, rate)
        :param local_tax_rate: Local tax rate as a decimal
        :param fica_rate: FICA tax rate as a decimal
        :param medicare_annual_cost: Annual cost of Medicare
        :param retirement_contribution_annual: Annual retirement contribution
        :param savings_rate: Savings rate as a decimal
        :param car_insurance_annual_cost: Annual cost of car insurance
        """
        self.gross_annual_salary = gross_annual_salary
        self.federal_tax_brackets = federal_tax_brackets
        self.state_tax_brackets = state_tax_brackets
        self.local_tax_rate = local_tax_rate
        self.fica_rate = fica_rate
        self.medicare_annual_cost = medicare_annual_cost
        self.retirement_contribution_annual = retirement_contribution_annual
        self.savings_rate = savings_rate
        self.car_insurance_annual_cost = car_insurance_annual_cost

    def calculate_federal_tax(self):
        """
        Calculate the federal tax based on the given tax brackets.

        :return: Total federal tax
        """
        federal_tax = 0
        previous_bracket_limit = 0

        # Iterate through each federal tax bracket
        for bracket_limit, rate in self.federal_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                # Calculate income within the current bracket
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                # Add the tax for this bracket to the total federal tax
                federal_tax += income_in_bracket * rate
                # Update the previous bracket limit
                previous_bracket_limit = bracket_limit
        return federal_tax

    def calculate_state_tax(self):
        """
        Calculate the state tax based on the given tax brackets.

        :return: Total state tax
        """
        state_tax = 0
        previous_bracket_limit = 0

        # Iterate through each state tax bracket
        for bracket_limit, rate in self.state_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                # Calculate income within the current bracket
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                # Add the tax for this bracket to the total state tax
                state_tax += income_in_bracket * rate
                # Update the previous bracket limit
                previous_bracket_limit = bracket_limit
        return state_tax

    def calculate_local_tax(self):
        """
        Calculate the local tax.

        :return: Total local tax
        """
        return self.gross_annual_salary * self.local_tax_rate

    def calculate_fica(self):
        """
        Calculate the FICA tax.

        :return: Total FICA tax
        """
        return self.gross_annual_salary * self.fica_rate

    def calculate_savings(self):
        """
        Calculate the savings amount.

        :return: Total savings amount
        """
        return self.gross_annual_salary * self.savings_rate

    def calculate_total_deductions(self):
        """
        Calculate the total deductions from the gross annual salary.

        :return: Total deductions
        """
        # Sum all the individual deductions
        return (
            self.calculate_federal_tax() +
            self.calculate_state_tax() +
            self.calculate_local_tax() +
            self.calculate_fica() +
            self.medicare_annual_cost +
            self.retirement_contribution_annual +
            self.calculate_savings() +
            self.car_insurance_annual_cost 
        )

    def calculate_net_annual_income(self):
        """
        Calculate the net annual income after all deductions.

        :return: Net annual income
        """
        # Subtract total deductions from gross annual salary
        return self.gross_annual_salary - self.calculate_total_deductions()

    def calculate_net_monthly_income(self):
        """
        Calculate the net monthly income after all deductions.

        :return: Net monthly income
        """
        # Divide net annual income by 12 to get monthly income
        return self.calculate_net_annual_income() / 12

    def print_summary(self):
        """
        Print a summary of the income calculations.
        """
        print("=" * 59)
        print("=" * 22 + " Gross Income " + "=" * 23)
        print("=" * 59)
        print(f"Gross Annual Salary: ${self.gross_annual_salary:.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 26 + " Taxes " + "=" * 26)
        print("=" * 59)
        print(f"Federal Tax: ${self.calculate_federal_tax():.2f}")
        print(f"State Tax: ${self.calculate_state_tax():.2f}")
        print(f"Local Tax: ${self.calculate_local_tax():.2f}")
        print(f"FICA: ${self.calculate_fica():.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 20 + " Health Insurance " + "=" * 21)
        print("=" * 59)
        print(f"Medicare: ${self.medicare_annual_cost:.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 23 + " Retirement " + "=" * 24)
        print("=" * 59)
        print(f"Company Retirement Contribution: ${self.retirement_contribution_annual:.2f}")
        print(f"Savings: ${self.calculate_savings():.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 22 + " Car Insurance " + "=" * 22)
        print("=" * 59)
        print(f"Car Insurance: ${self.car_insurance_annual_cost:.2f}")
        print("\n")


        print("=" * 59)
        print("=" * 25 + " Summary " + "=" * 25)
        print("=" * 59)
        print(f"Total Deductions: ${self.calculate_total_deductions():.2f}")
        print(f"Net Annual Income: ${self.calculate_net_annual_income():.2f}")
        print(f"Net Monthly Income: ${self.calculate_net_monthly_income():.2f}")
        print("\n")


class MortgageAndDebt:
    def __init__(self, rent, auto_payment, car_insurance, credit_card_payment):
        """
        Initialize the MortgageAndDebt with necessary parameters.

        :param rent: Monthly rent cost
        :param auto_payment: Monthly auto payment
        :param car_insurance: Monthly car insurance cost
        :param credit_card_payment: Monthly credit card payment
        """
        self.rent = rent
        self.auto_payment = auto_payment
        self.car_insurance = car_insurance
        self.credit_card_payment = credit_card_payment

    def calculate_total_monthly_debt(self):
        """
        Calculate the total monthly debt payments.

        :return: Total monthly debt payments
        """
        return self.rent + self.auto_payment + self.car_insurance + self.credit_card_payment

    def print_debt_summary(self):
        """
        Print a summary of the monthly debt payments.
        """
        print("=" * 59)
        print("=" * 26 + " Rent " + "=" * 27)
        print("=" * 59)
        print(f"Rent: ${self.rent:.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 24 + " Car Bills " + "=" * 24)
        print("=" * 59)
        print(f"Auto Payment: ${self.auto_payment:.2f}")
        print(f"Car Insurance: ${self.car_insurance:.2f}")
        print("\n")

        print("=" * 59)
        print("=" * 23 + " Credit Card " + "=" * 23)
        print("=" * 59)
        print(f"Credit Card Payment: ${self.credit_card_payment:.2f}")
        print("\n")
        

        print("=" * 59)
        print("=" * 19 + " Total Monthly Bills " + "=" * 19)
        print("=" * 59)
        print(f"Total Monthly Debt Payments: ${self.calculate_total_monthly_debt():.2f}")
        print("\n")


class Utilities:
    def __init__(self, gas_electric_car, electric_gas_house, sewer_water, internet, cellphone, entertainment, cable=0, landline=0):
        """
        Initialize the Utilities with necessary parameters.

        :param gas_electric_car: Monthly cost for gas/electric for car
        :param electric_gas_house: Monthly cost for electric and gas for house/apartment
        :param sewer_water: Monthly cost for sewer and water
        :param internet: Monthly cost for internet
        :param cellphone: Monthly cost for cellphone
        :param entertainment: Monthly cost for entertainment
        :param cable: Monthly cost for cable (default is 0)
        :param landline: Monthly cost for landline (default is 0)
        """
        self.gas_electric_car = gas_electric_car
        self.electric_gas_house = electric_gas_house
        self.sewer_water = sewer_water
        self.internet = internet
        self.cellphone = cellphone
        self.entertainment = entertainment
        self.cable = cable
        self.landline = landline

    def calculate_total_monthly_utilities(self):
        """
        Calculate the total monthly utility costs.

        :return: Total monthly utility costs
        """
        return self.gas_electric_car + self.electric_gas_house + self.sewer_water + self.internet + self.cellphone + self.entertainment + self.cable + self.landline

    def print_utilities_summary(self):
        """
        Print a summary of the monthly utility costs.
        """
        print("=" * 59)
        print("=" * 21 + " Utilities Bills " + "=" * 21)
        print("=" * 59)
        print(f"Gas/Electric for Car: ${self.gas_electric_car:.2f}")
        print(f"Electric/Gas for House: ${self.electric_gas_house:.2f}")
        print(f"Sewer and Water: ${self.sewer_water:.2f}")
        print(f"Internet: ${self.internet:.2f}")
        print(f"Cellphone: ${self.cellphone:.2f}")
        print(f"Entertainment: ${self.entertainment:.2f}")
        print(f"Cable: ${self.cable:.2f}")
        print(f"Landline: ${self.landline:.2f}")
        print(f"Total Monthly Utility and Entertainment Costs: ${self.calculate_total_monthly_utilities():.2f}")
        print("\n")


class MonthlyBudget:
    def __init__(self, monthly_net_income, mortgage_and_debt, utilities):
        """
        Initialize the MonthlyBudget with necessary parameters.

        :param monthly_net_income: Instance of MonthlyNetIncome
        :param mortgage_and_debt: Instance of MortgageAndDebt
        :param utilities: Instance of Utilities
        """
        self.monthly_net_income = monthly_net_income
        self.mortgage_and_debt = mortgage_and_debt
        self.utilities = utilities

    def calculate_leftover_money(self):
        """
        Calculate the leftover money after all monthly deductions.

        :return: Leftover money after all deductions
        """
        total_monthly_debt = self.mortgage_and_debt.calculate_total_monthly_debt()
        total_monthly_utilities = self.utilities.calculate_total_monthly_utilities()
        net_monthly_income = self.monthly_net_income.calculate_net_monthly_income()
        leftover_money = net_monthly_income - total_monthly_debt - total_monthly_utilities
        return leftover_money

    def print_budget_summary(self):
        """
        Print a summary of the budget calculations.
        """
        print("=" * 59)
        print("=" * 21 + " Leftover Money " + "=" * 22)
        print("=" * 59)
        print(f"Leftover Money after all deductions: ${self.calculate_leftover_money():.2f}")
        print("\n")


# Define your parameters
gross_annual_salary = 100300  # Updated based on your base pay
federal_tax_brackets = [
    (11000, 0.10),  # 10% on income up to $11,000
    (44725, 0.12),  # 12% on income between $11,001 and $44,725
    (95375, 0.22),  # 22% on income between $44,726 and $95,375
    (182100, 0.24)  # 24% on income between $95,376 and $182,100
]
state_tax_brackets = [
    (1000, 0.02),    # 2% on the first $1,000
    (2000, 0.04),    # 4% on income between $1,001 and $2,000
    (3000, 0.0475),  # 4.75% on income between $2,001 and $3,000
    (gross_annual_salary, 0.05)  # 5% on income above $3,000
]

# Maryland local tax rate (assuming the worst rate)
local_tax_rate = 0.032

# FICA tax rate
fica_rate = 0.062

# Your contributions (yearly)
medicare_annual_cost = 1454
retirement_contribution_annual = 8024  # Your contribution to the Northrop Grumman Savings Plan

# My personal choice for my retirement
savings_rate = 0.10

# Assumption for now
car_insurance_annual_cost = 330 * 12

# Create an instance of the MonthlyNetIncome class
monthly_net_income = MonthlyNetIncome(
    gross_annual_salary,
    federal_tax_brackets,
    state_tax_brackets,
    local_tax_rate,
    fica_rate,
    medicare_annual_cost,
    retirement_contribution_annual,
    savings_rate,
    car_insurance_annual_cost,
)

# Print the income summary
monthly_net_income.print_summary()

# Define mortgage and debt parameters
rent = 1500
auto_payment = 350
car_insurance = 350
credit_card_payment = 300

# Create an instance of the MortgageAndDebt class
mortgage_and_debt = MortgageAndDebt(
    rent,
    auto_payment,
    car_insurance,
    credit_card_payment
)

# Print the debt summary
mortgage_and_debt.print_debt_summary()

# Define utility parameters
gas_electric_car = 250    # Monthly cost for gas/electric for car
electric_gas_house = 75   # Monthly cost for electric and gas for house/apartment
sewer_water = 75          # Monthly cost for sewer and water
internet = 75             # Monthly cost for internet
cellphone = 30            # Monthly cost for cellphone
cable = 0                 # Monthly cost for cable (none for this case)
landline = 0              # Monthly cost for landline (none for this case)
entertainment = 43        # Monthly cost for entertainment (Spotify, Netflix, Hulu, ChatGPT, Apple iCloud) [$6, $10, $6, $20, $1]

# Create an instance of the Utilities class
utilities = Utilities(
    gas_electric_car,
    electric_gas_house,
    sewer_water,
    internet,
    cellphone,
    entertainment,
    cable,
    landline
)

# Print the utilities summary
utilities.print_utilities_summary()

# Create an instance of the MonthlyBudget class
monthly_budget = MonthlyBudget(monthly_net_income, mortgage_and_debt, utilities)

# Print the budget summary
monthly_budget.print_budget_summary()
