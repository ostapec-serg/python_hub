# 5. Write in one line the list generator (numbers in the range from 0 to 100), the sum of the digits
# of each element of which will be equal to 10.

generated_list = [i for i in range(0, 100) if i % 10 + i // 10 == 10]
print(generated_list)
