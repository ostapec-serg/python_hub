#3. Based on the previous function, create the following piece of code:
#    a) create a list with pairs of name / password of different types
#        -(follow the rules of your function) - both valid and not;
#    b) create a loop that will go through this loop and, using a validator,
#        -check this data and print a corresponding message for each
#        -pair of values, for example:
#Name: vasya
#Password: wasd
#Status: password must have at least one digit
#      -----
#Name: vasya
#Password: vasyapupkin2000
#Status: OK
#   P.S.  Don't forget use the block try/except ;)

from time import sleep

class UserNameException(Exception):
    pass

class PasswordException(Exception):
    pass


def validator(name, password):
    if name == '' or password == '':
        return "Username or password was not entered\n" \
               "Please, try again!!!"
    try:
        if 3 <= len(name) <= 50:
            if (8 <= len(password)) and \
                    any(map(str.isdigit, password)) and \
                    any(map(str.isalpha, password)) and \
                    any(map(str.isupper, password)):
                return True
            raise PasswordException

        raise UserNameException

    except UserNameException:
        return "Username or password was not entered\n" \
                      "Please, try again!!!"

    except PasswordException:
        return "Wrong password!\n" \
                   "- Password must be at least 8 characters!\n" \
                   "- At least  one characters must be uppercase!\n" \
                   "- Password must have at least one digit!"


def loop_validation(user_list):
    for item in user_list:
        username, password = item
        get_access = validator(username, password)
        if get_access is True:
            print(f"Name: {username}\n"
                  f"Password: {password}\n"
                  "Status: OK")
            sleep(0.5)
        else:
            print(f"Name: {username}\n"
                  f"Password: {password}\n"
                  f"Status: {get_access}")
            sleep(0.5)


users_list = [
    ("Emma", "22eMMa22"),
    ("John", "johnJohn"),
    ("Jake", "Jake1989"),
    ("Lisa", "Elisabeth90"),
    ("Tom", "10101"),
    ("James", "BondJamesBond"),
    ("Ed", "Eduardo85"),
    ("11111", "22222222"),
    ("", "somePass11"),
    ("someName", ""),
    ("", "")
]
loop_validation(users_list)
