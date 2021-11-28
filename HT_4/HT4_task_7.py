#7. Write a function that takes a list as input and counts the
#number of identical elements in it.

def count_func(our_list):
    duplicateFreq = {}
    for i in set(our_list):
        duplicateFreq[i] = our_list.count(i)
    for i in duplicateFreq:
        print(f"{i} repeats {duplicateFreq.get(i)} times")

yourString = input('Insert comma-separated values:\n').replace(" ","")
yourList = yourString.split(",")
count_func(yourList)
