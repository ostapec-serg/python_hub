#4. Write in one line the list generator (numbers in the range from 0 to 100), each element of
# which will be divide by 5 but will not be divide 3.

generated_list = [elem for elem in range(0, 100) if elem % 5 == 0 and elem % 3 != 0]
print(generated_list)
