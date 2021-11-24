# 5. The user enters the variables "x" and "y" with arbitrary numeric values;
# - Create a simple conditional construction (of course it must be in the body of the function),
# during the execution of which the equality of the variables "x" and "y"
#will be checked and if the variables "x" and "y" the difference of numbers is returned.
# Conditions is:
#- x> y;    the answer - x is greater than y on z
#- x <y;    the answer - y is greater than x on z
#- x == y. the answer - x is equal to z

def ratio(x_num, y_num):
    if x_num > y_num or x_num < y_num:
        result = abs(x_num - y_num)
        if x_num > y_num:
            return f"{x_num} more than {y_num} by {result}"
        else:
            return f"{y_num} more than {x_num} by {result}"
    elif x_num == y_num:
        result = x_num
        return f"{x_num} equal {result}"

first_num = float(input("Insert first number\n"))
second_num = float(input("Insert second number\n"))
print(ratio(first_num, second_num))
