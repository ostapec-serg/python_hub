#Write a function <is_prime> that will take 1 argument - a number from 0 to 1000, and that
#will return True if this number is prime, and False - if not

import math

def is_prime(n):
    if 0 < n <=1000:
        if (math.factorial(n-1)+1) % n!=0:
            return False
        else:
            return True
    else:
        return "Number from 0 to 1000 need!!! Try again!)"

print(is_prime(int(input("Insert number from 0 to 1000: \n"))))
