#3. Write a script to sum of the first n positive integers.

pos_num = int(input('Insert positive integer:\n'))
num_list = [i for i in range(pos_num + 1)]
print(sum(num_list))
