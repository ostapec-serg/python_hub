# 6. Write a script to check whether a specified value is contained in a
# group of values.

a = int(input('Insert integer_a:\n'))
b = int(input('Insert integer_b:\n'))
myList = []

for i in input('Isert comma-separated int:\n').split(','):
    myList.append(int(i))
print(a in myList, b in myList, sep='\n')
