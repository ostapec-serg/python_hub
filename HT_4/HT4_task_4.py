# 4. Write a function <prime_list>, which will take 2 arguments -
# the beginning and end of the range, and return a list of prime
# numbers within this range

def prime(start, end):
    lid = []
    for i in range(start, end+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lid.append(i)
    return lid
start_range = int(input("Enter the beginning of the range: \n"))
end_range = int(input("Enter the end of the range: \n"))
print(f"The prime list is:\n{prime(start_range, end_range)}")
