# 6. Everyone knows this function like <range>.
# Write your own implementation of the function.
#  P.S. Generator must return.

def value_func(stop, start=0, step=1):
    if step > 0:
        while start < stop:
            yield start
            start += step

for elem in value_func(5):
    print(elem)
