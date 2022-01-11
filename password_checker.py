
chars = r"'/  \ = '"


def check_my_password():

    if not any(characters.isupper() for characters in enter_password):
        print('Your password does not contain upper case')
    elif not any(characters.islower() for characters in enter_password):
        print('Your password does not contain any lower case')
    elif not any(characters.isdigit() for characters in enter_password):
        print('Your password must contain at least one digit')
    elif len(enter_password) < 8:
        print('Your password is less than 8 characters')
    elif len(enter_password) > 32:
        print('Your Password is more than 32 characters')
    elif any(characters.isspace() for characters in enter_password):
        print('Space(s) detected. Password should not contain any spaces')
    elif any((characters in chars) for characters in enter_password):
        print(r"Illegal character(s) found! Your password must not contain any of these characters / \ = ' ")
    else:
        print('Password accepted')
        print(f'Your Username is {enter_username}')
        return enter_password


class PasswordCheck:
    enter_password = ''
    enter_username = ''

    def __init__(self, enter_username, enter_password):
        self.password = enter_password
        self.username = enter_username


enter_username = input('Enter username: > ')

enter_password = input('Enter your password: > ')

checking_password = PasswordCheck(enter_username, enter_password)

check_my_password()
