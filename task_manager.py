# =====importing libraries===========
from datetime import date
from datetime import datetime
import os.path

# =====Login Section===========

# Set the variables
success = False
task_completion = "No"


BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

# Open the file for reading
users_file = open("user.txt", "r")
contents = users_file.read()
users_file.close()

# Convert a string file into the list
list_contents = contents.split("\n")

# Print the title
print(BOLD + BLUE + "««««««   login   »»»»»»\n" + END)

# The loop to request the login details from the users
while True:
    username = str(input("Please enter your username: "))
    password = str(input("Please enter your password: "))

    # A string variable which stores the entered username and password
    credentials = username + ", " + password

    # The loop for checking if the entered username and password are exist and store in the user.txt
    for i in range(0, len(list_contents)):
        if credentials.lower() == list_contents[i]:
            success = True

    # If the entered username and password are exist then the user is logged in
    if success:
        break

    # Error message
    else:
        print("——————————————————————————————————————————————————")
        print(RED + "\nInvalid username or password. Please try again.\n" + END)
        print("——————————————————————————————————————————————————")

# ==================================

# ======= Functions in Menu ========


# The function that is called when the user selects 'r' to register a user
def reg_user():
    # Set the variables within the function
    name_list = []
    name_exist = False

    # The loops to create the list with the usernames only
    for n in range(0, len(list_contents)):
        list_content = list_contents[n]
        name = list_content.split("\n")

        for j in range(0, len(name)):
            name_new = name[j].split(", ")
            name_list.append(name_new[0])

    # The loop for requesting the new details from the user
    while True:
        # Request input of a new username
        new_username = str(input("Please enter a new username: "))

        # The loop to check if the username already exists in the file 'user.txt'
        for k in range(0, len(name_list)):
            if new_username == name_list[k]:
                name_exist = True

        # Check if the username already exists (if this is true)
        if name_exist:
            print(RED + "\nThe entered username already exists. Please try again.\n" + END)
            break
        else:
            # Request input of a new password
            new_password = str(input("Please enter a new password: "))

            # Request input of password confirmation
            password_conf = str(input("Please confirm your password: "))

            # Check if the new password and confirmed password are the same
            if new_password == password_conf:

                # If they are the same, add (create) a new user to the user.txt file
                with open("user.txt", "a") as file:
                    file.write("\n" + new_username + ", " + new_password)
                    break
            else:
                print(RED + "\nThe passwords don't match. Please try again.\n" + END)


# The function that is called when a user selects 'a' to add a new task
def add_task():
    # Request the user to enter a username of the person whom the task is assigned to
    username_task = str(input("Please enter a username of the person whom the task is assigned to: "))

    # Request the user to enter a title of a task
    title_task = str(input("Please enter a title of a task: "))

    # Request the user to enter a description of the task
    des_task = str(input("Please enter a description of the task: "))

    # Request the user to enter the due date of the task
    due_date_task = str(input("Please enter the due date of the task : "))

    # Current date
    today = date.today()
    current_date = today.strftime("%d %B %Y")

    # Add all new data to the file task.txt
    with open("tasks.txt", "a") as file:
        file.write("\n" + username_task + ", " + title_task + ", " + des_task + ", " + current_date + ", "
                   + due_date_task + ", " + task_completion)

    print(GREEN + "\nThank you! You added the task." + END)


# The function that is called when users type 'va' to view all the tasks listed in 'tasks.txt'
def view_all(tasks):
    # Set the local variable
    output_va = ""

    # Read a line from the list of tasks and enumerate each task
    for position1, line in enumerate(tasks):
        # Split the lines where there are comma and space
        split_tasks = line.split(", ")

        # The block for systemizing the information for each task on the screen
        result = f"\n———————————————[{position1 + 1}]———————————————\n"
        result += "\n"
        result += f"Assigned to:        {split_tasks[0]}\n"
        result += f"Task:               {split_tasks[1]}\n"
        result += f"Assigned date:      {split_tasks[3]}\n"
        result += f"Due date:           {split_tasks[4]}\n"
        result += f"Task complete?      {split_tasks[5].strip()}\n"
        result += f"Task description:   {split_tasks[2]}"
        result += "\n"
        output_va += result

    # Print the results
    print(output_va)

    result = "——————————————————————————————————————————————————"
    print(result)


# The function that is called when users type 'vm' to view all the tasks that have been assigned to them
def view_mine(tasks):

    # Read a line from the list of tasks
    for position2, line in enumerate(tasks):

        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Check if the username of the person logged in is the same as the username which was read from the file
        if username == split_tasks[0]:
            # The block for systemizing and displaying the information for the admin tasks on the screen
            result = f"\n———————————————[{position2 + 1}]———————————————\n"
            result += "\n"
            result += f"Assigned to:        {split_tasks[0]}\n"
            result += f"Task:               {split_tasks[1]}\n"
            result += f"Assigned date:      {split_tasks[3]}\n"
            result += f"Due date:           {split_tasks[4]}\n"
            result += f"Task complete?      {split_tasks[5]}\n"
            result += f"Task description:   {split_tasks[2]}"
            result += "\n"
            output_vm = result
            print(output_vm)

    print("——————————————————————————————————————————————————")


# The function to edit the particular task
def edit_vm(tasks, user_name):
    # Set the local variables
    new_tasks_view = ""
    tasks_index = []

    # The loop to add the number of tasks of the user to the list
    for q in range(0, len(tasks)):
        if tasks[q].split(",")[0] == user_name:
            tasks_index.append(q + 1)

    # The loop to edit the task or return to the main menu
    while True:
        task_choice = input("\nPlease select a task number for editing (enter '-1' to return to the main menu): ")

        # Catch an input value error
        try:
            task_choice = int(task_choice)
        except ValueError:
            print(RED + "\nInvalid input." + END)
            continue

        # Check if return to the main menu
        if task_choice == -1:
            break

        # Check if the user choose the correct number of task
        if task_choice not in tasks_index:
            print(RED + "\nYou have selected an invalid option. Try again." + END)
            continue

        # The task which should be edited
        edit_tasks_view = tasks[task_choice - 1]

        # The loop to print the options to edit the task
        while True:
            output = f"\n————————————————————[SELECT AN OPTION]————————————————————\n"
            output += "1 - Edit due date \n"
            output += "2 - Edit username of the person to whom the task is assigned \n"
            output += "3 - Mark as complete \n"
            output += "——————————————————————————————————————————————————\n"

            choice = int(input(output))

            # Check if selected option is valid
            if choice <= 0 or choice >= 4:
                print("You have selected an invalid option. Try again.")
                continue

            # Check if the option is number one 'Edit due date'
            if choice == 1:
                split_tasks = edit_tasks_view.split(", ")
                split_tasks[4] = input("Please enter a new due date: ")
                new_tasks_view = ", ".join(split_tasks)
                tasks[task_choice - 1] = new_tasks_view

            # Check if the option is number two 'Edit username of the person to whom the task is assigned'
            elif choice == 2:
                split_tasks = edit_tasks_view.split(", ")
                split_tasks[0] = input("Please enter a new username of the person to whom the task is assigned : ")
                new_tasks_view = ", ".join(split_tasks)
                tasks[task_choice - 1] = new_tasks_view

            # Check if the option is number three 'Mark as complete'
            elif choice == 3:
                split_tasks = edit_tasks_view.split(", ")
                split_tasks[5] = "Yes\n"
                new_tasks_view = ", ".join(split_tasks)
                tasks[task_choice - 1] = new_tasks_view

            # Write to the file the edited data
            with open("tasks.txt", "r") as file1:
                data = file1.readlines()
                data[task_choice - 1] = new_tasks_view
            with open("tasks.txt", "w") as file1:
                file1.writelines(data)

            break


# The function to calculate the total number of completed tasks
def completed_tasks():
    # Set the local variable
    total_completed_tasks = 0

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # The loop to read the lines in the list
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Check if the task is completed
        if split_tasks[5].strip("\n").lower() == "yes":
            total_completed_tasks += 1

    return total_completed_tasks


# The function to calculate the total number of uncompleted tasks
def uncompleted_tasks():
    # Set the local variable
    total_uncompleted_tasks = 0

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # The loop to read the lines in the list
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Check if the task is uncompleted
        if split_tasks[5].strip("\n").lower() == "no":
            total_uncompleted_tasks += 1

    return total_uncompleted_tasks


# The function to calculate the total number of uncompleted and overdue tasks
def overdue_uncompleted_tasks():
    # Set a local variable
    overdue_uncompltd_tasks = 0

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # Current date
    today = datetime.now()

    # The loop to read the lines in the list
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Convert the string to date format
        due_date_object = datetime.strptime(split_tasks[4], "%d %B %Y")

        # Check if the task is uncompleted and overdue
        if split_tasks[5].strip("\n").lower() == "no" and due_date_object < today:
            overdue_uncompltd_tasks += 1

    return overdue_uncompltd_tasks


# The function to calculate the total number of overdue tasks
def overdue_tasks():
    # Set a local variable
    total_overdue_tasks = 0

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # Current date
    today = datetime.now()

    # The loop to read the lines in the list
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Convert the string to date format
        due_date_object = datetime.strptime(split_tasks[4], "%d %B %Y")

        # Check if the due date is passed
        if due_date_object < today:
            total_overdue_tasks += 1

    return total_overdue_tasks


# The function to calculate the total number of tasks
def total_num_tasks():

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # Calculate the total number of tasks and print out it
    total_number_tasks = len(tasks)

    return total_number_tasks


# The function to read the file with tasks
def read_tasks():

    tasks_read1 = open("tasks.txt", "r")
    tasks_view1 = tasks_read1.readlines()
    tasks_read1.close()

    return tasks_view1


# The function to calculate the number of tasks for the particular user
def user_num_tasks(user_name):
    # Set a local variable
    user_number_tasks = 0

    # Call the function to read the file with the tasks
    tasks = read_tasks()

    # The loop to calculate the number of tasks for the particular user
    for line in tasks:
        if user_name == line.split(",")[0]:
            user_number_tasks += 1

    return user_number_tasks


# The function to calculate the total number of users
def total_num_users():
    # Open the file for reading
    users_file_users = open("user.txt", "r")
    contents_users = users_file_users.read()
    users_file.close()

    # Convert a string file into the list
    list_contents_users = contents_users.split("\n")

    # Calculate the total number of users
    total_number_users = len(list_contents_users)

    return total_number_users


# The function to calculate the tasks assigned to the particular user that have been completed
def user_completed_tasks(user_name):
    # Set a local variable
    counter = 0

    # Read the file with the tasks
    tasks = read_tasks()

    # The total number of tasks assigned to that user
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Check if the task assigned to particular user has been completed
        if split_tasks[0] == user_name and split_tasks[5].strip("\n").lower() == "yes":
            counter += 1

    return counter


# The function to calculate the tasks assigned to the particular user that must still be completed
def user_uncompleted_tasks(user_name):
    # Set the local variable
    counter = 0

    # Read the file with the tasks
    tasks = read_tasks()

    # The total number of tasks assigned to that user
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Check if the task assigned to the particular user must still be completed
        if split_tasks[0] == user_name and split_tasks[5].strip("\n").lower() == "no":
            counter += 1

    return counter


# The function to calculate the tasks assigned to the particular user that have not yet been completed and are overdue
def user_overdue_uncompleted_tasks(user_name):
    # Set the local variable
    counter = 0

    # Read the file with the tasks
    tasks = read_tasks()

    # Current date
    today = datetime.now()

    # The total number of tasks assigned to that user
    for line in tasks:
        # Split the line where there are comma and space
        split_tasks = line.split(", ")

        # Convert string to date format
        due_date_object = datetime.strptime(split_tasks[4], "%d %B %Y")

        # Check if the tasks assigned to the particular user have not yet been completed and are overdue
        if split_tasks[0] == user_name and split_tasks[5].strip("\n").lower() == "no" and due_date_object < today:
            counter += 1

    return counter


def list_users():
    # Set the local variable
    list_users_list3 = []

    # Open the file for reading
    users_file1 = open("user.txt", "r")
    contents1 = users_file1.read()
    users_file1.close()

    # Convert string to the list with the data from the file 'user.txt'
    list_users_list = contents1.split("\n")
    list_users_list1 = ", ".join([str(item) for item in list_users_list])
    list_users_list2 = list_users_list1.split(", ")

    # Calculate the number of username in the file
    length = int(len(list_users_list2) / 2)

    # The loop to create the list with the usernames only
    for m in range(0, length):
        list_users_list3.append(list_users_list2[2*m])

    return list_users_list3


# The function to generate the report with the tasks overview
def generate_report_task_overview():

    # Calculate the percentage of uncompleted tasks
    percentage_uncompleted_tasks = round(((uncompleted_tasks() / total_num_tasks()) * 100), 1)

    # Calculate the percentage of overdue tasks
    percentage_overdue_tasks = round(((overdue_tasks() / total_num_tasks()) * 100), 1)

    # Add all new data to the file task_overview.txt
    with open("task_overview.txt", "w") as file:
        file.write("——————————————[TASKS OVERVIEW]—————————————————\n\n" +
                   f"The total number of tasks is: {total_num_tasks()}\n" +
                   f"The total number of completed tasks is: {completed_tasks()}\n" +
                   f"The total number of uncompleted tasks is: {uncompleted_tasks()}\n" +
                   f"The total number of tasks that haven't been completed and that are overdue is: " +
                   f"{overdue_uncompleted_tasks()}\n" + f"The percentage of tasks that are uncompleted is: "
                                                        f"{percentage_uncompleted_tasks}%\n" +
                   f"The percentage of tasks that are overdue is: {percentage_overdue_tasks}%\n")


# The function to generate the report with the users overview
def generate_report_user_overview():

    # Add all new data to the file user_overview.txt
    with open("user_overview.txt", "w") as file_user:
        file_user.write("——————————————[USER OVERVIEW]—————————————————\n\n" +
                        f"The total number of users is: {total_num_users()}\n" +
                        f"The total number of tasks is: {total_num_tasks()}\n")

        # The loop to enumerate the users and calculated the statistic data accordingly
        for position, user in enumerate(list_users()):
            # The percentage of the total number of tasks that have been assigned to that user
            percentage_user_tasks = round(((user_num_tasks(user) / total_num_tasks()) * 100), 1)

            # Total number of tasks per user
            user_total_tasks = user_num_tasks(user)

            if user_total_tasks != 0:

                # The percentage of the tasks assigned to user that have been completed
                percentage_user_completed_tasks = round(((user_completed_tasks(user) / user_total_tasks) * 100), 1)
                # The percentage of the tasks assigned to user that must still be completed
                percentage_user_uncompleted_tasks = round(((user_uncompleted_tasks(user) / user_total_tasks) * 100), 1)
                # The percentage of the tasks assigned to user that have not yet been completed and are overdue
                percentage_user_overdue_uncompleted_tasks = round(((user_overdue_uncompleted_tasks(user) /
                                                                    user_total_tasks) * 100), 1)
            else:

                percentage_user_completed_tasks = 0
                percentage_user_uncompleted_tasks = 0
                percentage_user_overdue_uncompleted_tasks = 0

            # Add all calculated statistic data to the file user_overview.txt
            file_user.write(
                f"\n———————————————[{position + 1}]———————————————\n"
                f"The total number of tasks assigned to the user {user}: "
                f"{user_num_tasks(user)}\n" +
                f"The percentage of the total number of tasks that have been assigned to the user "
                f"{user} is: {percentage_user_tasks}%\n" +
                f"The percentage of the tasks assigned that user {user} "
                f"that have been completed is: {percentage_user_completed_tasks}%\n" +
                f"The percentage of the tasks assigned that user {user} "
                f"that must still be completed is: {percentage_user_uncompleted_tasks}%\n" +
                f"The percentage of the tasks assigned that user {user} that have not yet been "
                f"completed and are overdue is: {percentage_user_overdue_uncompleted_tasks}%\n")

    print(GREEN + "\nThank you! You generated the report." + END)

# ======= Menu ========


# The loop for the menu list
while True:
    # Check if the user is admin
    if username.lower() == "admin":
        print(BOLD + BLUE + "\n««««««   Welcome to the admin menu   »»»»»»" + END)

        # Admin' variant of the menu with the additional option 's - Show statistics'
        menu_admin = input('''\nSelect one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

        # Check for the particular menu option
        if menu_admin == "r":
            print("——————————————————————————————————————————————————")

            # Call the function for registering a new user
            reg_user()

        elif menu_admin == "a":
            print("——————————————————————————————————————————————————")

            # Call the function to add a new task
            add_task()

            print("——————————————————————————————————————————————————")

        elif menu_admin == "va":

            # Call the function to read the tasks file
            tasks_list = read_tasks()

            # Call the function to display all tasks
            view_all(tasks_list)

        elif menu_admin == "vm":

            # Call the function to read the tasks file
            tasks_list = read_tasks()

            # Call the function to view user's tasks
            view_mine(tasks_list)

            # Call the function to edit user's tasks
            edit_vm(tasks_list, username.lower())

        elif menu_admin == "gr":

            # Call the functions to generate the reports
            generate_report_task_overview()
            generate_report_user_overview()

        elif menu_admin == "ds":

            # Set the variables
            path1 = "tasks_overview.txt"
            path2 = "user_overview.txt"

            # Set 'True' value that files 'tasks_overview.txt' and 'user_overview.txt' are exist
            check_file1 = os.path.isfile(path1)
            check_file2 = os.path.isfile(path2)

            # Check if the file 'tasks_overview.txt' is not exist
            if not check_file1:

                # Call the function to generate the report
                generate_report_task_overview()

            # Open the file for reading
            task_overview_read = open("task_overview.txt", "r")
            tasks_view = task_overview_read.read()
            print(tasks_view)
            task_overview_read.close()

            # Check if the file 'user_overview.txt' is not exist
            if not check_file2:

                # Call the function to generate the report
                generate_report_user_overview()

            # Open the file for reading
            users_overview_file = open("user_overview.txt", "r")
            contents = users_overview_file.read()
            print(contents)
            users_overview_file.close()

        elif menu_admin == 'e':
            print(BLUE + BOLD + "\n««««««   Goodbye!   »»»»»»" + END)
            exit()

        else:
            print("\n——————————————————————————————————————————————————")
            print(RED + "You have made a wrong choice. Please try again." + END)
            print("——————————————————————————————————————————————————")

    # Check if the user is not the admin
    else:
        print(BOLD + BLUE + "\n««««««   Welcome to the users' menu   »»»»»»" + END)

        # Present the menu to the user and making sure that the user input is converted to lower case
        menu = input('''\nSelect one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: ''').lower()

        # Check for the particular menu option
        if menu == "r":

            print("——————————————————————————————————————————————————")
            print(RED + "You are not allowed to register new users. \nPlease select another option." + END)
            print("——————————————————————————————————————————————————")

        elif menu == "a":

            print("——————————————————————————————————————————————————")

            # Call the function to add a new task
            add_task()

            print("——————————————————————————————————————————————————")

        elif menu == "va":

            # Call function to read the tasks file
            tasks_list = read_tasks()

            # Call the function to display all tasks
            view_all(tasks_list)

        elif menu == 'vm':

            # Call function to read the tasks file
            tasks_list = read_tasks()

            # Call the function to view user's tasks
            view_mine(tasks_list)

            # Call the function to edit user's tasks
            edit_vm(tasks_list, username.lower())

        elif menu == 'e':
            print(BLUE + BOLD + "\n««««««   Goodbye!   »»»»»»" + END)
            exit()

        else:
            print(RED + "You have made a wrong choice. Please try again." + END)
