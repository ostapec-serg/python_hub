# 2.Write a script that will run through a list of tuples and replace the last value for each tuple.
# The list of tuples can be hardcoded. The value to which the last element of the
# tuple is replaced is entered by the user.
# The value entered by the user can not be converted (leave a string).
# The number of elements in the tupels must be different.

def changeVal(a):
    newList = []
    for i in tuList:
        a = list(i)
        a[-1] = b
        d = tuple(a)
        newList.append(d)
    return newList

b = input("Insert value:\n")
tuList = [(57, 6, "val"), (50, 60, 70, "val"), (35, "val"), ("val",)]
print(changeVal(tuList))
