# 1 .Write a script which accepts a sequence of comma-separated numbers from
# user and generate a list and a tuple with those numbers.

numbers = input('Insert comma-separated numbers:\n').split(',')
my_tuple = tuple(numbers)
print(f"List : {numbers} \nTuple : {my_tuple}")
