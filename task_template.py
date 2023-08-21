#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime
import calendar

def user_to_dic(file):
    dic = {}
    with open(file, "r") as user_file:
        user_file_data = user_file.read()
        split_lines = user_file_data.splitlines()

        for each_line in split_lines:
            user_and_password = each_line.split(", ")
            dic[user_and_password[0]] = user_and_password[1]
    return dic

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
while True:
    user_dic = user_to_dic("user.txt")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # This reads the user file, checks if the user exists,
    # checks if the password matches the user and asks the user to try again if not
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
        pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        if username != "admin":
            print("Only username: 'admin' is allowed to view statistics. Please exit and login as 'admin'")
            continue

        new_username = input("Enter new username: ")

        while True:
            new_password = input("New password: ")
            confirm_password = input("Confirm password: ")

            if new_password == confirm_password:
                break
            else:
                print("Passwords do not match. Please try gain")
                continue

        with open("user.txt", "a") as user_file:
            user_file.write(f"\n{new_username}, {new_password}")

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        while True:
            user_dic = user_to_dic("user.txt")
            user_for_task = input("Enter username: ")

            if user_for_task not in user_dic:
                print("Username does not exist. Please try again")
                continue
            else: 
                break
        task_title = input("Enter task title: ")
        task_desrip = input("Enter task description: ")
        task_due_date = input("Enter the due date for the task: ")
        get_date = datetime.now()
        task_status = "No"
        today = (f"{get_date.day}  {calendar.month_name[get_date.month][:3]}  {get_date.year}")
        task_final = [user_for_task, task_title, task_desrip, today, task_due_date, task_status]

        with open("tasks.txt", "a") as task_file:
            task_file.write(f"\n{', '.join(task_final)}")

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        with open("tasks.txt", "r") as task_file:
            task_file_data = task_file.read()
            each_task = task_file_data.splitlines()
            line = "\u2500" * 70
            output_space = "\t" * 3

            for each_line in each_task:
                task_list = each_line.split(", ")
                print(f'''{line}\nTask:\t{output_space}{task_list[1]}\nAssigned to:{output_space}{task_list[0]}\nDate assigned:{output_space}{task_list[3]}\nDue date:{output_space}{task_list[4]}\nTask complete?{output_space}{task_list[5]}\nTask description:\n {task_list[2]}\n{line}\n''')
                

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        with open("tasks.txt", "r") as task_file:
            task_file_data = task_file.read()
            each_task = task_file_data.splitlines()
            line = "\u2500" * 70
            output_space = "\t" * 3
            
            for each_line in each_task:
                task_list = each_line.split(", ")
                if task_list[0] == username:
                    print(f'''{line}\nTask:\t{output_space}{task_list[1]}\nAssigned to:{output_space}{task_list[0]}\nDate assigned:{output_space}{task_list[3]}\nDue date:{output_space}{task_list[4]}\nTask complete?{output_space}{task_list[5]}\nTask description:\n {task_list[2]}\n{line}\n''')

    elif menu == 's':

        if username != "admin":
            print("Only username: 'admin' is allowed to register users. Please exit and login as 'admin'")
            continue

        with open("tasks.txt", "r") as task_file:
            task_file_data = task_file.read()
            each_task = task_file_data.splitlines()

            task_count = 0

            for each_line in each_task:
                task_count += 1

        with open("user.txt", "r") as user_file:
            user_file_data = user_file.read()
            each_user = user_file_data.splitlines()

            user_count = 0

            for each_line in each_user:
                user_count += 1
        
        print(f"Total number of tasks: {task_count}\nTotal number of users: {user_count}")

            

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")