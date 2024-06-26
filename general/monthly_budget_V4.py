from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
import sys


class MonthlyNetIncome:
    def __init__(self, gross_annual_salary, federal_tax_brackets, state_tax_brackets, local_tax_rate, fica_rate, medicare_annual_cost, retirement_contribution_annual, savings_rate, car_insurance_annual_cost):
        # Initialize the MonthlyNetIncome class with various financial parameters
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
        # Calculate the total federal tax based on the gross annual salary and federal tax brackets
        federal_tax = 0
        previous_bracket_limit = 0
        for bracket_limit, rate in self.federal_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                federal_tax += income_in_bracket * rate
                previous_bracket_limit = bracket_limit
        return federal_tax

    def calculate_state_tax(self):
        # Calculate the total state tax based on the gross annual salary and state tax brackets
        state_tax = 0
        previous_bracket_limit = 0
        for bracket_limit, rate in self.state_tax_brackets:
            if self.gross_annual_salary > previous_bracket_limit:
                income_in_bracket = min(self.gross_annual_salary, bracket_limit) - previous_bracket_limit
                state_tax += income_in_bracket * rate
                previous_bracket_limit = bracket_limit
        return state_tax

    def calculate_local_tax(self):
        # Calculate the total local tax based on the gross annual salary and local tax rate
        return self.gross_annual_salary * self.local_tax_rate

    def calculate_fica(self):
        # Calculate the FICA tax based on the gross annual salary and FICA rate
        return self.gross_annual_salary * self.fica_rate

    def calculate_savings(self):
        # Calculate the annual savings based on the gross annual salary and savings rate
        return self.gross_annual_salary * self.savings_rate

    def calculate_total_deductions(self):
        # Calculate the total deductions including federal tax, state tax, local tax, FICA, Medicare, retirement contribution, savings, and car insurance
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
        # Calculate the net annual income after all deductions
        return self.gross_annual_salary - self.calculate_total_deductions()

    def calculate_net_monthly_income(self):
        # Calculate the net monthly income based on the net annual income
        return self.calculate_net_annual_income() / 12

    def print_summary(self):
        # Print a detailed summary of the gross income, taxes, health insurance, retirement contributions, car insurance, and net income
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
        # Initialize the MortgageAndDebt class with various debt-related parameters
        self.rent = rent
        self.auto_payment = auto_payment
        self.car_insurance = car_insurance
        self.credit_card_payment = credit_card_payment

    def calculate_total_monthly_debt(self):
        # Calculate the total monthly debt including rent, auto payment, car insurance, and credit card payment
        return self.rent + self.auto_payment + self.car_insurance + self.credit_card_payment

    def print_debt_summary(self):
        # Print a detailed summary of the monthly debt payments
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
        # Initialize the Utilities class with various utility-related parameters
        self.gas_electric_car = gas_electric_car
        self.electric_gas_house = electric_gas_house
        self.sewer_water = sewer_water
        self.internet = internet
        self.cellphone = cellphone
        self.entertainment = entertainment
        self.cable = cable
        self.landline = landline

    def calculate_total_monthly_utilities(self):
        # Calculate the total monthly utility costs including gas/electric for car, electric/gas for house, sewer and water, internet, cellphone, entertainment, cable, and landline
        return self.gas_electric_car + self.electric_gas_house + self.sewer_water + self.internet + self.cellphone + self.entertainment + self.cable + self.landline

    def print_utilities_summary(self):
        # Print a detailed summary of the monthly utility and entertainment costs
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
        # Initialize the MonthlyBudget class with instances of MonthlyNetIncome, MortgageAndDebt, and Utilities
        self.monthly_net_income = monthly_net_income
        self.mortgage_and_debt = mortgage_and_debt
        self.utilities = utilities

    def calculate_leftover_money(self):
        # Calculate the leftover money after all monthly debt and utility costs are deducted from the net monthly income
        total_monthly_debt = self.mortgage_and_debt.calculate_total_monthly_debt()
        total_monthly_utilities = self.utilities.calculate_total_monthly_utilities()
        net_monthly_income = self.monthly_net_income.calculate_net_monthly_income()
        leftover_money = net_monthly_income - total_monthly_debt - total_monthly_utilities
        return leftover_money

    def print_budget_summary(self):
        # Print a detailed summary of the leftover money after all deductions
        print("=" * 59)
        print("=" * 21 + " Leftover Money " + "=" * 22)
        print("=" * 59)
        print(f"Leftover Money after all deductions: ${self.calculate_leftover_money():.2f}")
        print("\n")


class BudgetInputForm(QWidget):
    def __init__(self, budget_gui):
        # Initialize the BudgetInputForm class with a reference to the main BudgetGUI instance
        super().__init__()
        self.budget_gui = budget_gui
        self.init_ui()

    def init_ui(self):
        # Initialize the input form UI
        layout = QVBoxLayout()

        # Create a scroll area for the input form
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)

        # List of labels for the input fields
        labels = [
            "Gross Annual Salary", "Federal Tax Brackets", "State Tax Brackets", "Local Tax Rate", "FICA Rate",
            "Medicare Annual Cost", "Retirement Contribution Annual", "Savings Rate", "Car Insurance Annual Cost",
            "Rent", "Auto Payment", "Car Insurance", "Credit Card Payment",
            "Gas/Electric Car", "Electric/Gas House", "Sewer Water", "Internet", "Cellphone", "Entertainment", "Cable", "Landline"
        ]

        self.entries = {}
        for label in labels:
            # Create a row for each input field
            row = QWidget()
            row_layout = QHBoxLayout(row)

            lbl = QLabel(label, self)
            row_layout.addWidget(lbl)

            ent = QLineEdit(self)
            row_layout.addWidget(ent)

            scroll_layout.addWidget(row)
            self.entries[label] = ent

        # Create the Update Budget button
        update_button = QPushButton("Update Budget", self)
        update_button.clicked.connect(self.update_budget)
        scroll_layout.addWidget(update_button)

        scroll_area.setWidget(scroll_content)
        layout.addWidget(scroll_area)
        self.setLayout(layout)

    def update_budget(self):
        # Update the budget data with the values entered in the input form
        try:
            # Get the input values
            gross_annual_salary = float(self.entries["Gross Annual Salary"].text())
            federal_tax_brackets = eval(self.entries["Federal Tax Brackets"].text())
            state_tax_brackets = eval(self.entries["State Tax Brackets"].text())
            local_tax_rate = float(self.entries["Local Tax Rate"].text())
            fica_rate = float(self.entries["FICA Rate"].text())
            medicare_annual_cost = float(self.entries["Medicare Annual Cost"].text())
            retirement_contribution_annual = float(self.entries["Retirement Contribution Annual"].text())
            savings_rate = float(self.entries["Savings Rate"].text())
            car_insurance_annual_cost = float(self.entries["Car Insurance Annual Cost"].text())
            rent = float(self.entries["Rent"].text())
            auto_payment = float(self.entries["Auto Payment"].text())
            car_insurance = float(self.entries["Car Insurance"].text())
            credit_card_payment = float(self.entries["Credit Card Payment"].text())
            gas_electric_car = float(self.entries["Gas/Electric Car"].text())
            electric_gas_house = float(self.entries["Electric/Gas House"].text())
            sewer_water = float(self.entries["Sewer Water"].text())
            internet = float(self.entries["Internet"].text())
            cellphone = float(self.entries["Cellphone"].text())
            entertainment = float(self.entries["Entertainment"].text())
            cable = float(self.entries["Cable"].text())
            landline = float(self.entries["Landline"].text())

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
            # Print error message if updating budget fails
            print("Error updating budget:", e)


class BudgetGUI(QMainWindow):
    def __init__(self, monthly_net_income, mortgage_and_debt, utilities, period="Monthly"):
        # Initialize the BudgetGUI class with instances of MonthlyNetIncome, MortgageAndDebt, and Utilities
        super().__init__()
        self.setWindowTitle("Budget GUI")
        self.monthly_net_income = monthly_net_income
        self.mortgage_and_debt = mortgage_and_debt
        self.utilities = utilities
        self.period = period
        self.tooltip = None  # Initialize tooltip attribute
        self.init_ui()

    def init_ui(self):
        # Initialize the main GUI
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Add the input form to the left side
        input_form = BudgetInputForm(self)
        layout.addWidget(input_form)

        # Create the pie chart area
        self.figure = Figure(figsize=(6, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)

        layout.addWidget(self.canvas)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.create_pie_chart()

        self.canvas.mpl_connect('motion_notify_event', self.on_hover)

    def create_pie_chart(self):
        # Create the pie chart based on the budget data
        self.ax.clear()

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

        # Draw the pie chart
        wedges, texts, autotexts = self.ax.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=140, colors=colors)
        self.ax.axis('equal')
        self.canvas.draw()

    def on_hover(self, event):
        # Handle hover events over the pie chart to show detailed segments
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
                    self.tooltip.hide()

    def expand_taxes(self):
        # Expand the 'Taxes' segment to show detailed breakdown
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
        # Expand the 'Mortgage and Debt' segment to show detailed breakdown
        self.labels = ['Rent', 'Auto Payment', 'Credit Card Payment']
        self.sizes = [
            self.mortgage_and_debt.rent,
            self.mortgage_and_debt.auto_payment,
            self.mortgage_and_debt.credit_card_payment
        ]
        self.update_pie_chart()

    def expand_utilities(self):
        # Expand the 'Utilities' segment to show detailed breakdown
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
        # Expand the 'Free Money' segment to show detailed breakdown
        self.labels = ['Leftover', 'Retirement Funding']
        leftover_money = self.monthly_net_income.calculate_net_monthly_income() - self.mortgage_and_debt.calculate_total_monthly_debt() - self.utilities.calculate_total_monthly_utilities()
        retirement_funding = self.monthly_net_income.retirement_contribution_annual / 12
        self.sizes = [
            leftover_money,
            retirement_funding
        ]
        self.update_pie_chart()

    def restore_pie_chart(self):
        # Restore the pie chart to its original state
        self.labels = self.original_labels.copy()
        self.sizes = self.original_sizes.copy()
        self.update_pie_chart()

    def update_pie_chart(self):
        # Update the pie chart with the current labels and sizes
        self.ax.clear()
        colors = plt.cm.tab20(np.linspace(0, 1, len(self.labels)))
        wedges, texts, autotexts = self.ax.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=140, colors=colors)
        self.ax.axis('equal')
        self.canvas.draw()

    def show_tooltip(self, event, index):
        # Show a tooltip with detailed information when hovering over a segment
        if self.tooltip is None:
            self.tooltip = QLabel(self)
            self.tooltip.setStyleSheet("background-color: white; border: 1px solid black;")
            self.tooltip.setWindowFlags(QtCore.Qt.ToolTip)
        self.tooltip.setText(f"{self.labels[index]}: ${self.sizes[index]:.2f}")
        # Calculate the global position of the tooltip
        tooltip_x = self.canvas.geometry().x() + event.x
        tooltip_y = self.canvas.geometry().y() + event.y
        self.tooltip.move(tooltip_x, tooltip_y)
        self.tooltip.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

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

    # Create instances of MonthlyNetIncome, MortgageAndDebt, and Utilities with dummy data
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

    # Create an instance of BudgetGUI
    budget_gui = BudgetGUI(monthly_net_income, mortgage_and_debt, utilities)

    # Create the main window and set the BudgetGUI as the central widget
    main_window = QMainWindow()
    main_window.setCentralWidget(budget_gui)
    main_window.setWindowTitle("Budget Application")
    main_window.show()

    # Start the Qt event loop
    sys.exit(app.exec_())
