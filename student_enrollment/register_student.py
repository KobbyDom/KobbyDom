import datetime
import random
import csv


student_name_info = []
register_date = datetime.date.today()
db_date = datetime.datetime.now().strftime('%d/%m/%Y')


# creating a list for student information
def student_name_list():
    collect_student_name_info = student_name_info
    return collect_student_name_info


# creating initials
def add_name_initials():
    student_name_list()

    for initial_name in student_name_list():
        for first_letter in initial_name[0:1]:

            for second_name in student_name_list()[1:]:
                for second_letter in second_name[0:1]:
                    adding_name_initials = first_letter + second_letter
                    return adding_name_initials


# adding stripped name initials to date and random numbers
def create_student_id():
    my_date = datetime.datetime.now().strftime("%y")
    return add_name_initials() + my_date + str(random.randint(1, 10000))


# printing final results
def school_registration():
    print(f'Date:{register_date.today()}----ID:{create_student_id()}----First Name:{first_name}----'
          f'Middle Name:{middle_name}----Last Name:{last_name}')


# clear list
def clear_data():
    student_name_list().clear()


class RegisterStudent:

    def __init__(self, first_name, middle_name, last_name):
        self.student_first_name = first_name
        self.student_middle_name = middle_name
        self.student_last_name = last_name


# asking for user input for student registration
while True:
    clear_data()
    first_name = input('Type Student First Name. Type e to end registration: ').upper()
    student_name_info.append(first_name)
    if first_name == 'E':
        break

    middle_name = input('Type Student Middle Name: ').upper()
    student_name_info.append(middle_name)

    last_name = input('Type Student Last Name: ').upper()
    student_name_info.append(last_name)

    register_student = RegisterStudent(first_name, middle_name, last_name)

    school_registration()

    with open('student_id_register', mode='a', newline='') as f:
        column_names = ['Date', 'Student ID', 'First Name', 'Middle Name', 'Last Name']
        write_to_db = csv.DictWriter(f, fieldnames=column_names)

        # write_to_db.writeheader()
        write_to_db.writerow(
            {'Date': db_date, 'Student ID': create_student_id(),
             'First Name': first_name,
             'Middle Name': middle_name,
             'Last Name': last_name})
    print('Student Data Stores successfully')
    print('Thank You For Registering')



