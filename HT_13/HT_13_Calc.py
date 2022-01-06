class Calc(object):    """     class used to calculate two numbers. Integers or float    Attributes    last_resul: int or float        keep last operation result    __result: int or float        its private instance. Keep result of method calling,        until another method calling        used inside the class only    Methods    division(a, b)        divide two numbers    addition(a, b)        addition of two numbers    subtraction(a, b)        subtract two numbers    multiplication(a, b)        multiply two numbers    """    last_result = None    __result = None    @staticmethod    def __check_type(a, b):        """        Method __check_type is checkin type parameters a and b        __check_type is private method.        Used inside the class only        :param a: int or float        :param b: int or float        :return: True or False        """        if (type(a) is int or type(a) is float) \                and (type(b) is int or type(b) is float):            return True        else:            return False    @staticmethod    def division(a, b):        """        Method divide two numbers. Two parameters take        :param a: int or float            first number for division        :param b: int or float            second number for division        :return: result of operation        """        if Calc.__check_type(a, b) is True:            if b != 0:                operation_result = a / b                Calc.last_result = operation_result                if Calc.last_result is None:                    Calc.last_result = operation_result                return operation_result            else:                raise ZeroDivisionError("division by 0")        else:            raise TypeError("type must be int or float")    @staticmethod    def addition(a, b):        """        Method addition two numbers. Two parameters take        :param a: int or float            first number for addition        :param b: int or float            second number for addition        :return: result of operation        """        if Calc.__check_type(a, b) is True:            operation_result = a + b            Calc.last_result = operation_result            if Calc.last_result is None:                Calc.last_result = operation_result            return operation_result        else:            raise TypeError("type must be int or float")    @staticmethod    def subtraction(a, b):        """        Method subtract two numbers. Two parameters take        :param a: int or float            first number for subtract        :param b: int or float            second number for subtract        :return: result of operation        """        if Calc.__check_type(a, b) is True:            operation_result = a - b            Calc.last_result = operation_result            if Calc.last_result is None:                Calc.last_result = operation_result            return operation_result        else:            raise TypeError("type must be int or float")    @staticmethod    def multiplication(a, b):        """        Method multiply two numbers. Two parameters take        :param a: int or float            first number for multiply        :param b: int or float            second number for multiply        :return: result of operation        """        if Calc.__check_type(a, b) is True:            operation_result = a * b            Calc.last_result = operation_result            if Calc.last_result is None:                Calc.last_result = operation_result            return operation_result        else:            raise TypeError("type must be int or float")numbers = Calc()print(f"Last result is {numbers.last_result}")print(f"Result of division {numbers.division(10, 2)}")print(f"Last result is {numbers.last_result}")print(f"Result of addition {numbers.addition(10, 2)}")print(f"Last result is {numbers.last_result}")print(f"Result of subtraction {numbers.subtraction(10, 2)}")print(f"Last result is {numbers.last_result}")print(f"Result of multiplication {numbers.multiplication(10, 2)}")print(f"Last result is {numbers.last_result}")print(f"Last result is {numbers.last_result}")print(numbers.division(10, 0))