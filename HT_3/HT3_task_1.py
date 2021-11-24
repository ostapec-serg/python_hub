# 1. Create a loop from 0 to ... (entered by the user).
# Create a condition in the loop that will print the
# current value if the remainder of the division by 17 is 0

fin_int = int(input("Insert positive integer:\n"))
if fin_int <= 0:
    print("Áchtung!!! Positive integer need!!!")
for element in range(0, fin_int+1):
    if element%17 == 0:
        print(element)
