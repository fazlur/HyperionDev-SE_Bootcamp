# File I created (task_manager_art.py) to keep graphics and embellishment for menus. Find the file in the same folder
from task_manager_art import *

# Defining reg_user function
def reg_user():
    user_exist = True
    while True:
        read_user_file = open('user.txt', 'r')
        print(add_user_line)
        new_user = input("Username: ")
        current_line = 0

        # Reading file contents to user_register
        file = open('user.txt', 'r')
        user_register = file.readlines()
        file.close()
        
        print(user_register)

        while current_line <= len(user_register):
            line = user_register[current_line]
            print(line.split(',')[0].strip().lower())
            if current_line == len(user_register):
                user_exist = False
                break
            elif(line.split(',')[0].strip().lower() == new_user.lower()):
                print(duplicate_user)
                break
            else:
                current_line += 1

        if user_exist is False:
            # Getting password and confirming if they match
            while True:
                password = input("Password: ")
                password_retype = input("Retype Password: ")
                print(bottom_line)
                if password != password_retype:
                    print(wrong_password)
                else:
                    break


    # Writing the  username/password to file
    user_file_out = open('user.txt', 'a')
    user_file_out.write("\n" + new_user + ", " + password)
    user_file_out.close()