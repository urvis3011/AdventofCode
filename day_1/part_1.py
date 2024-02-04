file_path = "input.txt"

with open(file_path, 'r') as file:
    input = file.read()

# Split the input into lines
lines = input.strip().split('\n')

values = []
for line in lines:
    first = None
    last = None
    for char in line:
        if char.isdigit():
            last = char
            if first is None:
                first = char
    values.append(int(first + last))

# Sum up all the values
result = sum(values)

print("The sum of all values is:", result)

"""Assign last number then check is first is 
there or not if it’s empty or none then it gives 
the number to first then goes to next char in 
line does same till last char """
