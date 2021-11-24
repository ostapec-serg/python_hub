# 2. The user enters the initial and final year.
#Create a cycle that will display all leap years in this period (inclusive)

def leap_year(start_y, stop_y):
    for year in range(start_y, stop_y+1):
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            print(year)
start_year = int(input("Insert initial year:\n"))
stop_year = int(input("Insert final year:\n"))
leap_year(start_year, stop_year)
