# 6. Enter the number. If this number is positive, find its square,
# if negative, increase it by 100, if 0, do not change.

def sum_move(val):
    if val == 0:
        return val
    elif val < 0:
        return round(val + 100, 2)
    else:
        return round(val**2, 2)
print(sum_move(float(input("Enter the number: \n"))))
