# 2.Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The value to which the last element of the
# tuple is replaced is entered by the user.
# The value entered by the user can not be converted (leave a string).
# The number of elements in the tupels must be different.

def change_val(val):
    new_list = []
    in_val = input("Insert value:\n")
    for i in val:
        list_val = list(i)
        list_val[-1] = in_val
        tu_list = tuple(list_val)
        new_list.append(tu_list)
    return new_list

someList = [(57, 6, "val"), (50, 60, 70, "val"), (35, "val"), ("val",)]
print(change_val(someList))
