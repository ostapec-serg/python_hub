# 7. Well and traditionally -> the calculator :)
# there should be 1 function which would accept 3 arguments
#- one of which operation which to make!

print("""Operation is:\n(+)-addition, (-)-subtraction, (/)-division, (*)multiplication\n
(mod)-Modules, (pow)-Exponent, (div)-Floor division,\n
!!!Division by 0 is prohibited!!!""")
def calculac(num1, oper, num2):
    if oper == '+':
        s = num1 + num2
        return s
    elif oper == '-':
        s = num1 - num2
        return s
    elif oper == '*':
        s = num1 * num2
        return s
    elif oper == '/':
        if num2 != 0:
            s = num1 / num2
            return s
        else:
            return "Division by 0 is prohibited!"
    elif oper == 'div':
        if num2 != 0:
            s = num1 // num2
            return s
        else:
            return "Division by 0 is prohibited!!"
    elif oper == 'pow':
        s = num1 ** num2
        return s
    elif oper == 'mod':
        if num2 != 0:
            s = num1 % num2
            return s
        else:
            return "Division by 0 is prohibited!"
    else:
        return "Try again"
first_num = float(input("Insert first number that you want to use:\n"))
second_num = float(input("Insert second number that you want to use:\n"))
operation = input("Insert operation that you want to use:\n")
print(calculac(first_num , operation, second_num))
