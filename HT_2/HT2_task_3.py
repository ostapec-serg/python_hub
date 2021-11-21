#3. Write a script to remove an empty elements from a list

difTypeList = [(), ("hey"), ("",), ("ma", "ke", "my"), [''], {},
               ['d', 'a', 'y'], '', []]
print(list(filter(None, difTypeList)))
