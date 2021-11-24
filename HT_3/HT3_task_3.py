# 3. Write a season function that takes one argument -
#the number of the month (from 1 to 12), which will return the time of year
#to which the month belongs (winter, spring, summer or autumn)

def season(month):
    if  1 <= month <= 2 or month == 12:
        return "Winter"
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    if 9 <= month <= 11:
        return "Fall(Autumn)"

month_number = int(input('Insert month number(from 1 to 12):\n'))
print(season(month_number)
