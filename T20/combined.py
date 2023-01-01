# List to hold numbers from input files
input_numbers = []

# Opening files to read and append to a list as int for sorting later
with open('numbers1.txt', 'r') as file_in:
    for line in file_in:
        input_numbers.append(int(line))

with open('numbers2.txt', 'r') as file_in:
    for line in file_in:
        input_numbers.append(int(line))

# Sorting the numbers
input_numbers = sorted(input_numbers)

# Opening file for writing and looping through list and writing it to file
with open('all_numbers.txt', 'w') as file_out:
    for number in input_numbers:
        # Converting to str when writing to file and adding new line
        file_out.write(str(number) + "\n")