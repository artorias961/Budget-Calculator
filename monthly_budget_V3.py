import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class MonthlyNetIncome:
    def __init__(self, gross_annual_salary, federal_tax_brackets, state_tax_brackets, local_tax_rate, fica_rate, medicare_annual_cost, retirement_contribution_annual, savings_rate, car_insurance_annual_cost):
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
        federal_tax = 0
        previous_bracket_limit = 0
        for bracket_limit, rate in self.federal_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                federal_tax += income_in_bracket * rate
                previous_bracket_limit = bracket_limit
        return federal_tax

    def calculate_state_tax(self):
        state_tax = 0
        previous_bracket_limit = 0
        for bracket_limit, rate in self.state_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                state_tax += income_in_bracket * rate
                previous_bracket_limit = bracket_limit
        return state_tax

    def calculate_local_tax(self):
        return self.gross_annual_salary * self.local_tax_rate

    def calculate_fica(self):
        return self.gross_annual_salary * self.fica_rate

    def calculate_savings(self):
        return self.gross_annual_salary * self.savings_rate

    def calculate_total_deductions(self):
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
        return self.gross_annual_salary - self.calculate_total_deductions()

    def calculate_net_monthly_income(self):
        return self.calculate_net_annual_income() / 12

    def print_summary(self):
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
        self.rent = rent
        self.auto_payment = auto_payment
        self.car_insurance = car_insurance
        self.credit_card_payment = credit_card_payment

    def calculate_total_monthly_debt(self):
        return self.rent + self.auto_payment + self.car_insurance + self.credit_card_payment

    def print_debt_summary(self):
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
        self.gas_electric_car = gas_electric_car
        self.electric_gas_house = electric_gas_house
        self.sewer_water = sewer_water
        self.internet = internet
        self.cellphone = cellphone
        self.entertainment = entertainment
        self.cable = cable
        self.landline = landline

    def calculate_total_monthly_utilities(self):
        return self.gas_electric_car + self.electric_gas_house + self.sewer_water + self.internet + self.cellphone + self.entertainment + self.cable + self.landline

    def print_utilities_summary(self):
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
        self.monthly_net_income = monthly_net_income
        self.mortgage_and_debt = mortgage_and_debt
        self.utilities = utilities

    def calculate_leftover_money(self):
        total_monthly_debt = self.mortgage_and_debt.calculate_total_monthly_debt()
        total_monthly_utilities = self.utilities.calculate_total_monthly_utilities()
        net_monthly_income = self.monthly_net_income.calculate_net_monthly_income()
        leftover_money = net_monthly_income - total_monthly_debt - total_monthly_utilities
        return leftover_money

    def print_budget_summary(self):
        print("=" * 59)
        print("=" * 21 + " Leftover Money " + "=" * 22)
        print("=" * 59)
        print(f"Leftover Money after all deductions: ${self.calculate_leftover_money():.2f}")
        print("\n")


class BudgetInputForm:
    def __init__(self, root, budget_gui):
        self.root = root
        self.budget_gui = budget_gui

        # Create a canvas and a scrollbar
        self.canvas = tk.Canvas(root)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Layout
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Create the form fields
        self.create_form_fields()

    def create_form_fields(self):
        # Create and arrange the form fields in the scrollable frame
        labels = [
            "Gross Annual Salary", "Federal Tax Brackets", "State Tax Brackets", "Local Tax Rate", "FICA Rate",
            "Medicare Annual Cost", "Retirement Contribution Annual", "Savings Rate", "Car Insurance Annual Cost",
            "Rent", "Auto Payment", "Car Insurance", "Credit Card Payment",
            "Gas/Electric Car", "Electric/Gas House", "Sewer Water", "Internet", "Cellphone", "Entertainment", "Cable", "Landline"
        ]

        self.entries = {}
        for label in labels:
            row = ttk.Frame(self.scrollable_frame)
            row.pack(side="top", fill="x", padx=5, pady=5)

            lbl = ttk.Label(row, text=label, width=30, anchor='w')
            lbl.pack(side="left")

            ent = ttk.Entry(row)
            ent.pack(side="right", expand=True, fill="x")

            self.entries[label] = ent

        # Create the Update Budget button
        update_button = ttk.Button(self.scrollable_frame, text="Update Budget", command=self.update_budget)
        update_button.pack(padx=10, pady=10)

    def update_budget(self):
        try:
            # Get the input values
            gross_annual_salary = float(self.entries["Gross Annual Salary"].get())
            federal_tax_brackets = eval(self.entries["Federal Tax Brackets"].get())
            state_tax_brackets = eval(self.entries["State Tax Brackets"].get())
            local_tax_rate = float(self.entries["Local Tax Rate"].get())
            fica_rate = float(self.entries["FICA Rate"].get())
            medicare_annual_cost = float(self.entries["Medicare Annual Cost"].get())
            retirement_contribution_annual = float(self.entries["Retirement Contribution Annual"].get())
            savings_rate = float(self.entries["Savings Rate"].get())
            car_insurance_annual_cost = float(self.entries["Car Insurance Annual Cost"].get())
            rent = float(self.entries["Rent"].get())
            auto_payment = float(self.entries["Auto Payment"].get())
            car_insurance = float(self.entries["Car Insurance"].get())
            credit_card_payment = float(self.entries["Credit Card Payment"].get())
            gas_electric_car = float(self.entries["Gas/Electric Car"].get())
            electric_gas_house = float(self.entries["Electric/Gas House"].get())
            sewer_water = float(self.entries["Sewer Water"].get())
            internet = float(self.entries["Internet"].get())
            cellphone = float(self.entries["Cellphone"].get())
            entertainment = float(self.entries["Entertainment"].get())
            cable = float(self.entries["Cable"].get())
            landline = float(self.entries["Landline"].get())

            # Update the budget data
            self.budget_gui.monthly_net_income = MonthlyNetIncome(
                gross_annual_salary,
                federal_tax_brackets,
                state_tax_brackets,
                local_tax_rate,
                fica_rate,
                medicare_annual_cost,
                retirement_contribution_annual,
                savings_rate,
                car_insurance_annual_cost
            )
            self.budget_gui.mortgage_and_debt = MortgageAndDebt(rent, auto_payment, car_insurance, credit_card_payment)
            self.budget_gui.utilities = Utilities(
                gas_electric_car, electric_gas_house, sewer_water, internet, cellphone, entertainment, cable, landline
            )

            # Redraw the pie chart with updated data
            self.budget_gui.create_pie_chart()
        except Exception as e:
            print("Error updating budget:", e)


class BudgetGUI:
    def __init__(self, root, monthly_net_income, mortgage_and_debt, utilities, period="Monthly"):
        self.root = root  # Use the provided root window
        self.root.title("Budget GUI")
        self.monthly_net_income = monthly_net_income
        self.mortgage_and_debt = mortgage_and_debt
        self.utilities = utilities
        self.tooltip = None
        self.period = period
        self.create_widgets()

    def create_widgets(self):
        header_frame = ttk.Frame(self.root)
        header_frame.pack(padx=10, pady=10, fill=tk.X)

        header_label = ttk.Label(header_frame, text=f"{self.period} Budget", font=("Helvetica", 16))
        header_label.pack()

        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.create_pie_chart(frame)

        self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def create_pie_chart(self, frame=None):
        fig = Figure(figsize=(6, 6), dpi=100)
        self.ax = fig.add_subplot(111)

        net_monthly_income = self.monthly_net_income.calculate_net_monthly_income()
        total_monthly_debt = self.mortgage_and_debt.calculate_total_monthly_debt()
        total_monthly_utilities = self.utilities.calculate_total_monthly_utilities()
        leftover_money = net_monthly_income - total_monthly_debt - total_monthly_utilities

        total_taxes = (
            self.monthly_net_income.calculate_federal_tax() +
            self.monthly_net_income.calculate_state_tax() +
            self.monthly_net_income.calculate_local_tax() +
            self.monthly_net_income.calculate_fica() +
            self.monthly_net_income.medicare_annual_cost
        ) / 12

        mortgage_and_debt = self.mortgage_and_debt.calculate_total_monthly_debt()

        utilities = self.utilities.calculate_total_monthly_utilities()

        free_money = leftover_money + (self.monthly_net_income.retirement_contribution_annual / 12)

        self.labels = ['Taxes', 'Mortgage and Debt', 'Utilities', 'Free Money']
        self.sizes = [
            total_taxes,
            mortgage_and_debt,
            utilities,
            free_money
        ]

        self.original_labels = self.labels.copy()
        self.original_sizes = self.sizes.copy()

        colors = plt.cm.tab20(np.linspace(0, 1, len(self.labels)))

        wedges, texts, autotexts = self.ax.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=140, colors=colors)
        self.ax.axis('equal')

        if frame is not None:
            self.canvas = FigureCanvasTkAgg(fig, master=frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def on_hover(self, event):
        if event.inaxes == self.ax:
            for i, wedge in enumerate(self.ax.patches):
                if wedge.contains_point([event.x, event.y]):
                    if self.labels[i] == 'Taxes':
                        self.expand_taxes()
                    elif self.labels[i] == 'Mortgage and Debt':
                        self.expand_mortgage_and_debt()
                    elif self.labels[i] == 'Utilities':
                        self.expand_utilities()
                    elif self.labels[i] == 'Free Money':
                        self.expand_free_money()
                    else:
                        self.show_tooltip(event, i)
                    break
            else:
                self.restore_pie_chart()
                if self.tooltip:
                    self.tooltip.destroy()
                    self.tooltip = None

    def expand_taxes(self):
        self.labels = ['Federal Tax', 'State Tax', 'Local Tax', 'FICA', 'Medicare']
        self.sizes = [
            self.monthly_net_income.calculate_federal_tax() / 12,
            self.monthly_net_income.calculate_state_tax() / 12,
            self.monthly_net_income.calculate_local_tax() / 12,
            self.monthly_net_income.calculate_fica() / 12,
            self.monthly_net_income.medicare_annual_cost / 12
        ]
        self.update_pie_chart()

    def expand_mortgage_and_debt(self):
        self.labels = ['Rent', 'Auto Payment', 'Credit Card Payment']
        self.sizes = [
            self.mortgage_and_debt.rent,
            self.mortgage_and_debt.auto_payment,
            self.mortgage_and_debt.credit_card_payment
        ]
        self.update_pie_chart()

    def expand_utilities(self):
        self.labels = ['Car Gas/Electric', 'Electric and Gas (Home)', 'Cable', 'Internet', 'Cellphone', 'Sewer and Water']
        self.sizes = [
            self.utilities.gas_electric_car,
            self.utilities.electric_gas_house,
            self.utilities.cable,
            self.utilities.internet,
            self.utilities.cellphone,
            self.utilities.sewer_water
        ]
        self.update_pie_chart()

    def expand_free_money(self):
        self.labels = ['Leftover', 'Retirement Funding']
        leftover_money = self.monthly_net_income.calculate_net_monthly_income() - self.mortgage_and_debt.calculate_total_monthly_debt() - self.utilities.calculate_total_monthly_utilities()
        retirement_funding = self.monthly_net_income.retirement_contribution_annual / 12
        self.sizes = [
            leftover_money,
            retirement_funding
        ]
        self.update_pie_chart()

    def restore_pie_chart(self):
        self.labels = self.original_labels.copy()
        self.sizes = self.original_sizes.copy()
        self.update_pie_chart()

    def update_pie_chart(self):
        self.ax.clear()
        colors = plt.cm.tab20(np.linspace(0, 1, len(self.labels)))
        wedges, texts, autotexts = self.ax.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=140, colors=colors)
        self.ax.axis('equal')
        self.canvas.draw()

    def show_tooltip(self, event, index):
        if self.tooltip:
            self.tooltip.destroy()
        self.tooltip = tk.Toplevel(self.root)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{self.root.winfo_pointerx()+10}+{self.root.winfo_pointery()+10}")
        tooltip_text = f"{self.labels[index]}: ${self.sizes[index]:.2f}"
        label = ttk.Label(self.tooltip, text=tooltip_text, background="white", relief="solid", borderwidth=1)
        label.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Budget Application")

    # Initialize with dummy data
    gross_annual_salary = 100300
    federal_tax_brackets = [(11000, 0.10), (44725, 0.12), (95375, 0.22), (182100, 0.24)]
    state_tax_brackets = [(1000, 0.02), (2000, 0.04), (3000, 0.0475), (gross_annual_salary, 0.05)]
    local_tax_rate = 0.032
    fica_rate = 0.062
    medicare_annual_cost = 1454
    retirement_contribution_annual = 8024
    savings_rate = 0.10
    car_insurance_annual_cost = 330 * 12

    rent = 1500
    auto_payment = 350
    car_insurance = 350
    credit_card_payment = 300

    gas_electric_car = 250
    electric_gas_house = 75
    sewer_water = 75
    internet = 75
    cellphone = 30
    entertainment = 43
    cable = 0
    landline = 0

    monthly_net_income = MonthlyNetIncome(
        gross_annual_salary,
        federal_tax_brackets,
        state_tax_brackets,
        local_tax_rate,
        fica_rate,
        medicare_annual_cost,
        retirement_contribution_annual,
        savings_rate,
        car_insurance_annual_cost
    )
    mortgage_and_debt = MortgageAndDebt(rent, auto_payment, car_insurance, credit_card_payment)
    utilities = Utilities(gas_electric_car, electric_gas_house, sewer_water, internet, cellphone, entertainment, cable, landline)

    budget_gui = BudgetGUI(root, monthly_net_income, mortgage_and_debt, utilities)
    input_form = BudgetInputForm(root, budget_gui)

    root.mainloop()
