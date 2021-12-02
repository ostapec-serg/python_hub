# 7. Implement a generator that picks up any iterable sequence
#(string, list, tuple) and returns a generator that will return values from
#that sequence, and if the last element in the sequence has been returned,
#the iteration begins again. For example:
#>>>for elem in generator([1, 2, 3]):
#   ...    print(elem)
#   ...
#   1
#   2
#   3
#  1
#   2
#   3
#   1
#   .......


from time import sleep

def generator(lst):
    while True:
        for item in lst:
            yield item
        sleep(0.5)
input_list = ([x.strip() for x in input('Insert comma-separated values:\n').split(",")])
for i in generator(input_list):
    print(i)
