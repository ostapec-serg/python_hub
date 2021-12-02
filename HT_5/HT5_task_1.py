# 1. Create a function with a list of five inside
# users (username and password).
# The function must take three arguments: two are required
# (<username> and <password>) and the third is an optional parameter
# <silent> (default value is <False>).
# The logic is as follows:
# if the correct name / password pair is entered - <True> is returned;
# if the wrong name / password and <silent> == <True> pair is entered
# - function returns <False>, otherwise (<silent> == <False>) -
# the LoginException exception is generated

class LoginException(Exception):
    pass

def valid_login(username, password, silent=False):
    users_list = [
        ("Emma", "121212"),
        ("John", "212121"),
        ("Jake", "111111"),
        ("Lisa", "222222"),
        ("Tom", "10101"),
    ]

    if (username, password) in users_list and (silent is False):
        return True
    elif  (username, password) not in users_list and (silent is False):
        return False

    raise LoginException

loginName = input("Enter user name:\n")
accountPass = input("Enter password:\n")
print(valid_login(loginName, accountPass))
