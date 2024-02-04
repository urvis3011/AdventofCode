nums = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

# Initialize the total sum
values = 0

file_path = "input.txt"

with open(file_path, 'r') as file:
    input = file.read()

lines = input.strip().split('\n')

for line in lines:
    first = None
    last = None
    added_chars = ""

    for char in line:
        digit = None

        # Check if the character is a digit
        if char.isdigit():
            digit = char
        else:
            # Accumulate characters to identify spelled-out numbers
            added_chars += char

            # Check if accumulated characters match a spelled-out number
            for spelled_number, dig in nums.items():
                if added_chars.endswith(spelled_number):
                    digit = str(dig)

        if digit is not None:
            last = digit
            if first is None:
                first = digit

    values += int(first + last)

# Print the result
print("The sum of all values is:", values)
