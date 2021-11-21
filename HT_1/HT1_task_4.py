#4. Write a script to concatenate N strings.

n_string = int(input("Insert number N strigs:\n"))
result = ""

for i in range(n_string):
    current_string = input("Insert your string:\n")
    result += current_string

print("Concatenate N strings is:", result)
