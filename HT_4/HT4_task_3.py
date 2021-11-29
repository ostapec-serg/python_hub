#Write a function <is_prime> that will take 1 argument - a number from 0 to 1000, and that
#will return True if this number is prime, and False - if not

def is_prime(num):
    if 0 < num  <= 1000:
        return all(num % i for i in range(2, a))
    else:
        return "Number from 0 to 1000 need!!! Try again!)"

print(is_prime(int(input("Insert number from 0 to 1000: \n"))))
