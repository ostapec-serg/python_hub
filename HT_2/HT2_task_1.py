#1. Write a script to concatenate all elements in a list into a string
# and print it. List must be include strings and integers!

startList = [1, 4, "word", 32, "age", "name", 21]
print(''.join(str(elem) for elem in startList))
