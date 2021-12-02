# 6. Everyone knows this function like <range>.
# Write your own implementation of the function.
#  P.S. Generator must return.

def value_func(start: int,stop=0,step=1):
    if stop+1 == start:
        yield []
    else:
        if start == stop:
            yield []
        else:
            if step > 0:
                if stop == 0:
                    stop = start
                    start = 0
                while start < stop:
                    yield start
                    start += step
            elif (step < 0) and (stop < 0):
                if stop == 0:
                    stop = start
                    start = 0
                while start > stop:
                    yield start
                    start += step
            elif step == 0:
                raise ValueError("step cannot be 0")
            else:
                yield []

for elem in value_func(10):
    print(elem)
