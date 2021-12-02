#2. Create a function to validate the name / password pair according to the following rules:
#    - the name must be not less than 3 characters and not more than 50;
#    - the password must be at least 8 characters and must have at least one digit;
#    - something of your own :)
#  If any of the parameters do not meet the requirements - create an exception
# with the appropriate text

class UserNameException(Exception):
    pass

class PasswordException(Exception):
    pass


def validator(name, password):
    if  (name == '') or (password == ''):
        return "Username or password was not entered\n" \
               "Please, try again!!!"

    try:
        if 3 <= len(name) <= 50:
                if (8 <= len(password)) and \
                            any(map(str.isdigit, password)) and \
                            any(map(str.isalpha, password)) and \
                            any(map(str.isupper, password)):
                        return "Registration succesed!"
                raise PasswordException

        raise  UserNameException

    except UserNameException:
            return "Wrong Username!\n " \
               "-Username must be not less than 3 characters " \
                   "and not more than 50!"

    except PasswordException:
            return "Wrong password!\n" \
                   "- Password must be at least 8 characters!\n" \
                   "- At least  one characters must be uppercase!\n" \
                   "- Password must have at least one digit!"


loginName = input("Enter user name:\n")
accountPass = input("Enter password:\n")
print(validator(loginName, accountPass))
