#8.Write a script to generate and print a dictionary that contains a
#number  in the form (x, x*x)

intVal = int(input("Insert positive integer:\n"))
generetedDict = {i:i**2 for i in range(intVal + 1)}
print(generetedDict)
