# 6. Create a function that will receive strings and handle the following cases:
#- if the line length is in the range 30-50 -> prints the length, number of letters and numbers
#- if the length is less than 30 -> prints the sum of all numbers and
# a separate line without numbers (only with letters)
#- if the length is more than 50 -> your imagination

def strings_processing(string):
    len_str = len(string)
    extra_alpha = ''.join(filter(str.isalpha, string))
    extra_int = ''.join(filter(str.isdigit, string))
    if 30 <= len_str <= 50:
        print(f"String length:{len_str}\n"
              f"Num of letters:{len(extra_alpha)}\n"
              f"Num of digits:{len(extra_int)}")
    elif len_str < 30:
        num_list = [int(i) for i in extra_int]
        print(f"Sum of all digits:{sum(num_list)}\nString is: {extra_alpha}")
    elif len_str > 50:
        print("_HAPPY NEW YEAR_")
        for i in range(8, 0, -1):
            print(" " * (i - 1), end="")
            print("" * (((8 - i) * 2) + 1))

strings_processing(input("Insert your string here:\n"))
