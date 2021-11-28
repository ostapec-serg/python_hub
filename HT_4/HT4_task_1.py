#1. Write a function <square>, which will take one argument - the side of the square, and
# return 3 values (tuple): the perimeter of the square, the area of the square and its diagonal.

import math

def square(sq):
    return 4 * sq, sq ** 2, round(math.sqrt(2 * sq ** 2), 2)

result = square(int(input("Enter the side of the square:\n")))
print(result,'\n' f"Perimeter of the square is: {result[0]}\n"
             f"The area of the square is: {result[1]}\n"
             f"Diagonal of the square is: {result[2]}")
