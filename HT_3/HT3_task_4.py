# 4. Create 3 different functions (of your choice).
# Each of these functions must return some result.
#Also create fourth functions, which in the body calls the previous 3, processes returned by them
# result and also returns the result. So we will
# call 1 function, and it has 3 more in its body

def some_1_func(a=8):
    result_1 = a * some_3_func()
    result = result_1 + some_2_func()
    return round(result, 2)
def some_2_func(c=53):
    result_2 = c * (c / some_3_func())
    return round(result_2, 2)
def some_3_func(e=5):
    result_3 = e * (e * 3)   # or (e * float(input()) for interactive mode
    return round(result_3, 2)
def some_func4():
    all_result = some_1_func(), some_2_func(), some_3_func()
    out_list = []
    for elem in all_result:
        print(elem)
        out_list.append(elem)
    return out_list
print(round(sum(some_func4()), 2))
