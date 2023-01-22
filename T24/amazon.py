# Defining empty lists that will later hold the min, max and avg lists values

min_list = []
max_list = []
avg_list = []

# Defining functions to find min, max and average from lists of integers

def min(list):
    # Starting the variable that will hold the smallest number with the 1st element of the list
    min_num = list[0]  
    # Looping through list and comparing each element with the 1st, if smaller update the min_num variable
    for num in range(0, len(list)):
        if list[num] < min_num:
            min_num =  list[num]

    return min_num

def max(list):
    # Starting the variable that will hold the biggest number with the 1st element of the list
    max_num = list[0]  
    # Looping through list and comparing each element with the 1st, if bigger update the min_num variable
    for num in range(0, len(list)):
        if list[num] > max_num:
            max_num =  list[num]
    return max_num

def avg(list):
    avg_num = sum(list) / len(list)
    return avg_num



# Reading the file with 'utf-8-sig' to remove the first character of the file

with open("input.txt", "r",  encoding='utf-8-sig') as file_read:
    for line in file_read:
        # Getting the name of the operation before ":"
        if line.split(":")[0].lower() == "min":
            # Getting the values after the ":", splitting them by "," and creating lists with those values
            # using strip() to get rid of the carriage return
            min_list = line.strip().split(":")[1].split(",")
            # Converting the from string to list, by looping each element and converting it
            min_list = [int(i) for i in min_list]
        elif line.split(":")[0].lower() == "max":
            max_list = line.strip().split(":")[1].split(",") 
            # Converting the from string to list, by looping each element and converting it
            max_list = [int(i) for i in max_list]
        elif line.split(":")[0].lower() == "avg":
            avg_list = line.strip().split(":")[1].split(",") 
            # Converting the from string to list, by looping each element and converting it
            avg_list = [int(i) for i in avg_list]
            

# Writing to file by first checking if the lists have any values, and if there are values execute the 
# previously defined functions and write them to file
with open("output.txt", "w") as file_write:
    if len(min_list) > 0:
        file_write.write(f'''The min of {min_list} is {min(min_list)}\n''')
    if len(max_list) > 0:
        file_write.write(f'''The max of {max_list} is {max(max_list)}\n''')
    if len(avg_list) > 0:
        file_write.write(f'''The avg of {avg_list} is {avg(avg_list)}\n''')
