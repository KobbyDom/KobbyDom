from grading_system import school_courses, general_subjects
import datetime as dt

grading_list = []

subject_list = []

subject_marks = []

# school courses with corresponding subjects
school_course = {

    1: ['French',
        'Geography',
        'Literature',
        'Economics',
        'History',
        'Government',
        'RME'
        ],

    2: ['Biology',
        'Chemistry',
        'Physics',
        'Elective Maths'
        ]
}


def grading():
    if 80.00 <= assign_subject_marks <= 100.00:
        my_grades = 'Grade A+'
        grading_list.append(my_grades)
    elif 75.00 <= assign_subject_marks <= 79.99:
        my_grades = 'Grade B+'
        grading_list.append(my_grades)
    elif 65.00 <= assign_subject_marks <= 74.99:
        my_grades = 'Grade B'
        grading_list.append(my_grades)
    elif 60.00 <= assign_subject_marks <= 64.99:
        my_grades = 'Grade C'
        grading_list.append(my_grades)
    elif 50.00 <= assign_subject_marks <= 59.99:
        my_grades = 'Grade D'
        grading_list.append(my_grades)
    elif 00.00 <= assign_subject_marks <= 49.99:
        my_grades = 'Grade F'
        grading_list.append(my_grades)
    else:
        my_grades = 'Incomplete'
        grading_list.append(my_grades)


school_courses()


select_course = int(input('Please select course using course number:> '))

# fetch the values(subjects) from the dict based on selected key(Course)
display_select_course = school_course[select_course]

# display subject selected
for i, subjects in enumerate(display_select_course, start=1):
    print(i, subjects)

# adding selected subjects to list
while True:
    add_subjects = int(input('Add subjects by selecting subject number:> '))
    adding_course = display_select_course[add_subjects - 1]
    subject_list.append(adding_course)

    if len(subject_list) == 3:
        subject_list.extend(general_subjects())
        print()
        for numbering, my_subjects in enumerate(subject_list, start=1):
            print(numbering, my_subjects)

        length_of_subject_list = len(subject_list)
        length_of_marks_list = len(subject_marks)

        while length_of_marks_list < length_of_subject_list:
            assign_subject_marks = float(input('Assign subject marks:> '))
            grading()
            subject_marks.append(assign_subject_marks)
            length_of_marks_list += 1
        break

if length_of_marks_list == length_of_subject_list:
    print(f'Terminal Report for {dt.date.year} Academic Year')
    for subjects, student_marks, grades in zip(subject_list, subject_marks, grading_list):
        print('{}----------{}--({})'.format(subjects, student_marks, grades))
    print('Examination report successfully generated!!!')
print(f'Report printed on {dt.datetime.today()}')
