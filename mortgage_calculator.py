
# Calculating mortgage payment

banks = ['GCB', 'ADB', 'CMG', 'Fidelity Bank', 'CAL Bank']

banks_and_rates = {1: 6, 2: 7, 3: 10, 4: 9}

for i, my_banks in enumerate(banks, start=1):
    print(i, my_banks)


def compute_loan_deduction():
    compute_bank_rate = (get_bank_rate / 100) / 12

    loan_years_to_months = loan_year * 12

    numerator_computation = (compute_bank_rate * (1 + compute_bank_rate) ** loan_years_to_months)

    denominator_computation = (1 + compute_bank_rate) ** loan_years_to_months - 1

    final_monthly_computation = (enter_loan_amount * (numerator_computation / denominator_computation))
    return round(final_monthly_computation, 2)


class MonthlyLoan:
    def __init__(self, select_bank, enter_loan_amount, loan_year):
        self.bank = select_bank
        self.amount = enter_loan_amount
        self.year = loan_year


print()
select_bank = int(input("Please select bank eg '1':> "))

while True:
    enter_loan_amount = float(input('Please enter loan amount:> '))
    if enter_loan_amount < 10_000:
        print('Your loan amount should not be below GH¢10,000.00')

    else:
        loan_year = int(input('Please enter loan years:> '))
        break

get_bank_rate = banks_and_rates.get(select_bank)

my_loan = MonthlyLoan(select_bank, enter_loan_amount, loan_year)
compute_loan_deduction()

print(f'Your monthly deduction for a mortgage of GH¢{enter_loan_amount:,} is GH¢{compute_loan_deduction():,}')

