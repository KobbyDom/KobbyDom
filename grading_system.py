# grading_list = []


# school grading system
def marks_grading(grading_list, assign_subject_marks):
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
        return my_grades


def school_courses():
    courses = ['General Arts',
               'Science',
               'Visual Arts',
               'Home Economics',
               'Business'
               ]

    for numbering, subjects in enumerate(courses, start=1):
        print(numbering, subjects)


def general_subjects():
    core_subject_list = [
        'Mathematics',
        'General Science',
        'English',
        'Computer Science',
        'Social Science'
    ]
    return core_subject_list

    # for numbering, my_subjects in enumerate(subject_list, start=1):
    #     print(numbering, my_subjects)
