# Income Bands As At 2018
first_cum_income = 319
next_cum_income_1 = 419
next_cum_income_2 = 539
next_cum_income_3 = 3539
next_cum_income_4 = 20000

# Income Rates As At 2018
Rate_1 = 0.00
Rate_2 = 0.05
Rate_3 = 0.10
Rate_4 = 0.175
Rate_5 = 0.25
Rate_6 = 0.30

ssf_contribution = 0

taxable_income = 0

gross_salary = 0

staff_rank = ''

print('''
1. Director
2. Deputy Director
3. Manager
''')
try:
    staff_rank = int(input("Please Select Your Rank eg 1:  "))
    print("*" * 35)
except ValueError as e:
    print('Position selected does not exist. Please try again')
#####################################################################################################################
# Directors' allowances and allowance rates
director_basic_salary = float(3500)
director_allowance = ["Entertainment Allowance", "Responsibility Allowance",
                      "Clothing Allowance", "House Help Allowance", "Fuel Allowance", "Risk Allowance"]
director_allowance_rate = [director_basic_salary * 0.20, director_basic_salary * 0.05,
                           director_basic_salary * 0.20, director_basic_salary * 0.10,
                           director_basic_salary * 0.20, director_basic_salary * 0.10]
#####################################################################################################################
# Deputy Directors' allowances and allowance rates
deputy_dir_basic_salary = float(3000)
deputy_dir_allowance = ["Clothing Allowance", "House Help Allowance",
                        "Fuel Allowance", "Risk Allowance"]
deputy_dir_allowance_rate = [deputy_dir_basic_salary * 0.20, deputy_dir_basic_salary * 0.10,
                             deputy_dir_basic_salary * 0.20, deputy_dir_basic_salary * 0.10]
#####################################################################################################################
# Managers' allowances and allowance rates
manager_basic_salary = float(2500)
manager_allowance = ["Clothing Allowance", "House Help Allowance",
                     "Fuel Allowance", "Risk Allowance"]
manager_allowance_rate = [manager_basic_salary * 0.20, manager_basic_salary * 0.10,
                          manager_basic_salary * 0.20, manager_basic_salary * 0.10]
#####################################################################################################################
# Matching list of director's allowances to allowance rates
director_total_allowance = 0
if staff_rank == 1:
    print(f'Basic Salary--------------------------------------GH¢{director_basic_salary:,}')
    for dir_allowa, dir_rate in zip(director_allowance, director_allowance_rate):
        print('{}-----GH¢{}'.format(dir_allowa, dir_rate))

# Computing total allowances for directors
    for total_allowance_rate in director_allowance_rate:
        director_total_allowance += total_allowance_rate

# Matching list of deputy director's allowances to allowance rates
deputy_dir_total_allowance = 0
if staff_rank == 2:
    print(f'Basic Salary---------------------------------------GH¢{deputy_dir_basic_salary:,}')
    for deputy_dir_allowa, deputy_dir_rate in zip(deputy_dir_allowance, deputy_dir_allowance_rate):
        print('{}-----GH¢{}'.format(deputy_dir_allowa, deputy_dir_rate))

# Computing total allowances for deputy directors
    for total_allowance_rate in deputy_dir_allowance_rate:
        deputy_dir_total_allowance += total_allowance_rate

# Matching list of manager's allowances to allowance rates
manager_total_allowance = 0
if staff_rank == 3:
    print(f'Basic Salary---------------------------------------GH¢{manager_basic_salary:,}')
    for manager_allowa, manager_rate in zip(manager_allowance, manager_allowance_rate):
        print('{}-----GH¢{}'.format(manager_allowa, manager_rate))

# Computing total allowances for managers
    for total_allowance_rate in manager_allowance_rate:
        manager_total_allowance += total_allowance_rate
#####################################################################################################################
# Computation of Director's Gross Salary
director_gross_salary = 0
if staff_rank == 1:
    print(f'Total Allowance -----------------------------------GH¢{director_total_allowance:,}')
    director_gross_salary = director_basic_salary + director_total_allowance
    print(f'Gross Salary --------------------------------------GH¢{director_gross_salary:,}')

# Computation of Deputy Director's Gross Salary
deputy_dir_gross_salary = 0
if staff_rank == 2:
    print(f'Total Allowance ----------------------------------GH¢{deputy_dir_total_allowance:,}')
    deputy_dir_gross_salary = deputy_dir_basic_salary + deputy_dir_total_allowance
    print(f'Gross Salary -------------------------------------GH¢{deputy_dir_gross_salary:,}')

# Computation of Manager's Gross Salary
manager_gross_salary = 0
if staff_rank == 3:
    print(f'Total Allowance -----------------------------------GH¢{manager_total_allowance:,}')
    manager_gross_salary = manager_basic_salary + manager_total_allowance
    print(f'Gross Salary --------------------------------------GH¢{manager_gross_salary:,}')

#####################################################################################################################
# Computation of SSF Contribution
director_ssf_contribution = 0
if staff_rank == 1:
    director_ssf_contribution = (director_basic_salary * 0.055)
    # print(f'SSF Contribution --------------------------------(GH¢{director_ssf_contribution})')

# Computation of SSF Contribution
deputy_director_ssf_contribution = 0
if staff_rank == 2:
    deputy_director_ssf_contribution = (deputy_dir_basic_salary * 0.055)
    # print(f'SSF Contribution --------------------------------(GH¢{deputy_director_ssf_contribution})')

manager_ssf_contribution = 0
if staff_rank == 3:
    manager_ssf_contribution = (manager_basic_salary * 0.055)
    # print(f'SSF Contribution ---------------------------------(GH¢{manager_ssf_contribution})')
#####################################################################################################################
# Computation of Taxable Income
if staff_rank == 1:
    taxable_income = (director_gross_salary - director_ssf_contribution)
    # print(f'Taxable Income -----------------------------------GH¢{taxable_income}')

# Computation of Deputy Director Taxable Income
if staff_rank == 2:
    taxable_income = (deputy_dir_gross_salary - deputy_director_ssf_contribution)
    # print(f'Taxable Income -----------------------------------GH¢{taxable_income}')

# Computation of Manager Taxable Income
if staff_rank == 3:
    taxable_income = (manager_gross_salary - manager_ssf_contribution)
    # print(f'Taxable Income -----------------------------------GH¢{taxable_income}')

#####################################################################################################################
# Computation of Income Tax on Taxable Income
def staff_income_tax():
    if taxable_income < first_cum_income:
        tax = Rate_1 * taxable_income

    elif taxable_income < next_cum_income_1:
        tax = Rate_1 * first_cum_income + Rate_2 * (taxable_income - first_cum_income)

    elif taxable_income < next_cum_income_2:
        tax = Rate_1 * first_cum_income + Rate_2 * (next_cum_income_1 - first_cum_income) + Rate_3 * \
              (taxable_income - next_cum_income_1)

    elif taxable_income < next_cum_income_3:
        tax = Rate_1 * first_cum_income + Rate_2 * (next_cum_income_1 - first_cum_income) + Rate_3 * \
              (next_cum_income_2 - next_cum_income_1) + Rate_4 * (taxable_income - next_cum_income_2)

    elif taxable_income < next_cum_income_4:
        tax = Rate_1 * first_cum_income + Rate_2 * (next_cum_income_1 - first_cum_income) + Rate_3 * \
              (next_cum_income_2 - next_cum_income_1) + Rate_4 * \
              (next_cum_income_3 - next_cum_income_2) + Rate_5 * (taxable_income - next_cum_income_3)

    else:
        tax = taxable_income * Rate_6

    return tax
#######################################################################################################################
# print(f'Income Tax --------------------------------------(GH¢{staff_income_tax()})')
#######################################################################################################################

if staff_rank == 1:
    print('Deductions:')
    print(f'SSF Contribution---------------GH¢{director_ssf_contribution:,}\n'
          f'Income Tax---------------------GH¢{staff_income_tax():,}')
    director_total_deductions = director_ssf_contribution + staff_income_tax()
    print(f'Total Deductions---------------------------------(GH¢{director_total_deductions:,})')
    director_net_salary = director_gross_salary - director_total_deductions
    print(f'Net Salary ---------------------------------------GH¢{director_net_salary:,}')
#######################################################################################################################
if staff_rank == 2:
    print('Deductions:')
    print(f'SSF Contribution---------------GH¢{deputy_director_ssf_contribution:,}\n'
          f'Income Tax---------------------GH¢{staff_income_tax():,}')
    deputy_director_total_deductions = deputy_director_ssf_contribution + staff_income_tax()
    print(f'Total Deductions --------------------------------(GH¢{deputy_director_total_deductions:,})')
    deputy_director_net_salary = deputy_dir_gross_salary - deputy_director_total_deductions
    print(f'Net Salary ---------------------------------------GH¢{deputy_director_net_salary:,}')
#######################################################################################################################
if staff_rank == 3:
    print('Deductions:')
    print(f'SSF Contribution---------------GH¢{manager_ssf_contribution:,}\n'
          f'Income Tax---------------------GH¢{staff_income_tax():,}')
    manager_total_deductions = manager_ssf_contribution + staff_income_tax()
    print(f'Total Deductions ---------------------------------(GH¢{manager_total_deductions:,})')
    manager_net_salary = manager_gross_salary - manager_total_deductions
    print(f'Net Salary ----------------------------------------GH¢{manager_net_salary:,}')

