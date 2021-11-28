#8. Write a function that will implement the logic of cyclic shift of elements in the list.
#That is, the function takes two arguments: the list and the amount of offset
#(if this value is positive - move from end to beginning,
#if negative - on the contrary - move the elements from the beginning of the list to its end).


def shift(seq, o_set=0):
    a = o_set % len(seq)
    return seq[-a:] + seq[:-a]
income_list = [4, 5, 0, "new", "some_val", (3, 4, 5), [6, 7, 8, 9]]
offset = int(input("Enter the length of the offset: \n"))
print(shift(income_list, offset))
