# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
import calendar

# ====functions section==============

# Converts the user.txt into a dictionary
# with usernames as keys and passwords as values


def user_to_dic(file):
    dic = {}
    with open(file, "r") as user_file:
        user_file_data = user_file.read()
        split_lines = user_file_data.splitlines()

        for each_line in split_lines:
            user_and_password = each_line.split(", ")
            dic[user_and_password[0]] = user_and_password[1]
    return dic

# Converts any .txt file into a list of lines


def split_lines(file):
    file_data = file.read()
    line_list = file_data.splitlines()
    return line_list

# Defining characters that will be required for the desired output format


line = "\u2500" * 70
output_space = "\t" * 3

# ====Login Section====
# This block of code allows a user to login.
while True:
    user_dic = user_to_dic("user.txt")

    username = input("Enter username: ")
    password = input("Enter password: ")

    # This reads the user file, checks if the user exists,
    # checks if the password matches the user
    # and asks the user to try again if it does not
    if username not in user_dic:
        print("Username does not exist. Please try again")
        continue
    if user_dic[username] != password:
        print("Incorrect password entered. Please try again")
        continue
    if user_dic[username] == password:
        print("Welcome\n")
        break

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
s - statistics
: ''').lower()

    if menu == 'r':

        # This code block will add a new user to the user.txt file

        # Restricts access to only 'admin'
        if username != "admin":
            print(''''Only username: admin is allowed to register new users.
Please exit and login as admin''')
            continue

        new_username = input("Enter new username: ")

        # Creates a new password for the new user
        # Has a password confirmation feature
        while True:
            new_password = input("New password: ")
            confirm_password = input("Confirm password: ")

            if new_password == confirm_password:
                break
            else:
                print("Passwords do not match. Please try gain")
                continue

        # Writes the new user to the user.txt file
        with open("user.txt", "a") as user_file:
            user_file.write(f"\n{new_username}, {new_password}")

    elif menu == 'a':

        # This code block will allow a user to add a new task to task.txt file
        while True:
            user_dic = user_to_dic("user.txt")
            user_for_task = input("Enter username: ")

            # Checks if the user exists by looking for it in the dictionary
            if user_for_task not in user_dic:
                print("Username does not exist. Please try again")
                continue
            else:
                break

        # Asks the user for the required details of the task
        task_title = input("Enter task title: ")
        task_desrip = input("Enter task description: ")
        task_due_date = input("Enter the due date for the task: ")
        get_date = datetime.now()
        task_status = "No"
        this_month = calendar.month_name[get_date.month][:3]
        today = (f"{get_date.day}  {this_month}  {get_date.year}")

        # Gathers all the user input into a list that will eventually be joined
        task_final = [user_for_task, task_title, task_desrip, today,
                      task_due_date, task_status]

        # Writes the task to the task.txt file by joining the list in a string
        with open("tasks.txt", "a") as task_file:
            task_file.write(f"\n{', '.join(task_final)}")

    elif menu == 'va':
        pass
        # This code block will read the task from task.txt file and
        with open("tasks.txt", "r") as task_file:

            each_task = split_lines(task_file)

            # Loops through each task in tasks.txt
            # and prints the details in the desired format
            for each_line in each_task:
                task_list = each_line.split(", ")
                print(f'''{line}\nTask:\t{output_space}{task_list[1]}
Assigned to:{output_space}{task_list[0]}
Date assigned:{output_space}{task_list[3]}
Due date:{output_space}{task_list[4]}
Task complete?{output_space}{task_list[5]}
Task description:\n {task_list[2]}\n{line}\n''')

    elif menu == 'vm':
        pass
        # This code block will read the task from task.txt file and

        with open("tasks.txt", "r") as task_file:

            each_task = split_lines(task_file)

            # Loops through the current users tasks and prints the details
            for each_line in each_task:
                task_list = each_line.split(", ")
                if task_list[0] == username:
                    print(f'''{line}\nTask:\t{output_space}{task_list[1]}
Assigned to:{output_space}{task_list[0]}
Date assigned:{output_space}{task_list[3]}
Due date:{output_space}{task_list[4]}
Task complete?{output_space}{task_list[5]}
Task description:\n {task_list[2]}\n{line}\n''')

    # This code displays company dtatistics to the admin only
    elif menu == 's':

        # Restricts access to admin only
        if username != "admin":
            print(''''Only username: 'admin' is allowed to view statistics. '
Please exit and login as 'admin''')
            continue

        with open("tasks.txt", "r") as task_file:

            each_task = split_lines(task_file)

            task_count = 0

            # Counts the number of tasks as it loops through each task
            for each_line in each_task:
                task_count += 1

        with open("user.txt", "r") as user_file:

            each_user = split_lines(user_file)

            user_count = 0

            # Counts the number of users as it loops through each user
            for each_line in each_user:
                user_count += 1

        print(f''''Total number of tasks: {task_count}
Total number of users: {user_count}''')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
