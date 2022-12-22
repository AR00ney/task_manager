#=====importing libraries===========
from datetime import date
from datetime import datetime
import os.path

# set variables
users = []
passwords = []
pair = 0
task = 0

# define a fuction to list users and passwords
def read_users(users, passwords):
    # open user.txt in read as f
    with open('user.txt', 'r') as f:
    # for loop for lines in f
        for line in f:
            # replace commmas for a empty char
            user = line.replace(',', '')
            # strip to remove \n
            user = user.strip()
            # split to create list
            user = user.split()
            # add user name to users
            users.append(user[0])
            # add user password to passwords
            passwords.append(user[1])

# define fuction to get todays date and display in wanted format
def get_today():
    # get todays date with imported datetime
        today = date.today()
        # format to wanted output
        today = today.strftime('%d %b %Y')
        today = datetime.strptime(today, '%d %b %Y').date()
        return today

# define fuction to log in user
def login(users, passwords):
    # while True
    while True:
        # get user input username
        user_login = input('Please enter your username:                        ')
        # check is username is in users
        if user_login in users:
            # for loop for range of user list
            for i in range(0, len(users)):
                # if user index i is equal to user_login
                if users[i] == user_login:
                    # i equals pair
                    pair = i
            # while True 
            while True:
                # get user input password
                user_password = input('Please enter your password or \'b\' to go back:      ')
                # if passward index i is equal to user_password return pair 
                if passwords[pair] == user_password:
                    return pair
                # if input is equal to back break this loop
                elif user_password == 'b':
                    break
                # if input equal to e return 'e'
                elif user_password == 'e':
                    return 'e'
                # else password wrong
                else:
                    # print incorrect password and continue loop
                    print('''========================================================
          Incorrect password please try again
========================================================''')
                    continue
        elif user_login == 'e':
            return 'e'
        # else user not found and continue loop
        else:
            print('User not found')
            continue

# define a fuction to show admin menu
def admin_menu():
    menu = input('''========================================================
        Select one of the following Options below:
                 r - Registering a user
                   a - Adding a task
                  va - View all tasks
                   vm - View my task
                  g - Generate reports
                  d - Display reports
                     s - Statistics
                        e - Exit
========================================================
:                           ''').lower()
    return menu

# define fuction to show user menu
def stand_menu():
    menu = input('''========================================================
        Select one of the following Options below:
                 r - Registering a user
                   a - Adding a task
                  va - View all tasks
                   vm - View my task
                       e - Exit
========================================================
:                           ''').lower()
    return menu

# define fuction to regsister a new user
def reg_user(users, passwords):
            # reset users
            users = []
            # call read_users fuction
            read_users(users, passwords)

            # while True
            while True:
                # get input new user
                new_user = input('''========================================================
Enter new username:               ''')
                # check if username taken and continue if True
                if new_user in users:
                    print('''========================================================
                    Username taken''')
                    continue
                # while True
                while True:
                    # get input new password
                    new_pass = input('''========================================================
                Please enter a password
        The password must be 5 - 11 characters long
Enter a password:                ''')
                    # if password if greater than 11 print pass too long and continue
                    if len(new_pass) > 11:
                        print('''========================================================
                    ! ERROR !
                Password too long
========================================================''')
                        continue
                    # else if pass is less than 5 print too short and continue 
                    elif len(new_pass) < 5:
                        print('''========================================================
                    ! ERROR !
                Password to short
========================================================''')
                        continue
                    # else confirm pass
                    else:
                        confirm_pass = input('Confirm password:                ')
                        # if new_pass and confirm_pass match break
                        if new_pass == confirm_pass:
                            print('''========================================================
                  User added to system''')
                            break
                        # else passwords don't match continue
                        else:
                            print('''========================================================
                Passwords do not match''')
                            continue    
                # open user.txt append as f
                with open('user.txt', 'a') as f:
                    # write with new line with f string in format 'name, password'
                    f.write(f'\n{new_user}, {new_pass}')
                return 

# define function to add task to task.txt
def add_task(users, passwords):
    # reset users 
    users = []
    # call read_users to repeat user list to catch any new added users
    read_users(users, passwords)

    # while True
    while True:
        # get input user to assign task
        new_task_user = input('User to assign task:                  ')
        # check if user is in users
        if new_task_user not in users:
            # if not print user not found and continue
            print('User not found')
            continue
        # else user is in users break
        else:
            break
    # get input new task title and description
    new_task_title = input('task title:                           ')
    new_task_descrip = input('task description:                     ')
        
    while True:
        # get user input new task date 
        new_task_date = input('Enter task date EG:07 Nov 2022:       ')
        # if date is not 11 characters ask to re enter in correct format and continue
        if len(new_task_date) != 11:
            print('''Please enter date in format:          01 Jan 2023''')
            continue
        # else format ok break
        else:
            break
    # get todays date with imported datetime
    today = date.today()
    # format to wanted output
    today = today.strftime('%d %b %Y')
    # set to complete to 'no'
    complete = 'No'
    # open tasks.txt append as f
    with open('tasks.txt', 'a') as f:
        # write in wanted format and print task added continue to menu
        f.write(f'\n{new_task_user}, {new_task_title}, {new_task_descrip}, {today}, {new_task_date}, {complete}')
        print('''========================================================
                        Task added''')
        return

# define function to veiw all tasks
def view_all():
    task = 0
    # open tasks.txt read as f
    with open('tasks.txt', 'r') as f:
        # for loop line in f task + 1 split by ', ' and print in wanted format
        for line in f:
            task += 1
            line = line.split(', ')
            print(f'''              Task {task}
------------------------------------------------------------------------------
Task:                   {line[1]}
------------------------------------------------------------------------------
Assigned to:            {line[0]}
------------------------------------------------------------------------------
Date assigned:          {line[3]}
------------------------------------------------------------------------------
Due Date:               {line[4]}
------------------------------------------------------------------------------
Task Complete?          {line[-1]}
------------------------------------------------------------------------------
Task description:
    {line[2]}
------------------------------------------------------------------------------
''')  
        # reset task variable
        task = 0
        return 

# define function to view own tasks
def view_mine(users, pair):
    # create variables
    task = 0
    content = []
    new_file = ''

    # open tasks.txt read as f
    with open('tasks.txt', 'r') as f:
        # for loop line in f split by ', '
        for line in f:
            line = line.strip()
            line = line.split(', ')
            # add all lines to content in 2D list
            content += [line]
            # count tasks
            task += 1
            # if task is for user print in wanted format
            if users[pair] == line[0]:
                print(f'''              Task {task}

Task:                   {line[1]}
------------------------------------------------------------------------------
Assigned to:            {line[0]}
------------------------------------------------------------------------------
Date assigned:          {line[3]}
------------------------------------------------------------------------------
Due Date:               {line[4]}
------------------------------------------------------------------------------
Task Complete?          {line[-1]}
------------------------------------------------------------------------------
Task description:
    {line[2]}
------------------------------------------------------------------------------
''') 
        # while True
        while True:
            # get user input to select a task to edit
            edit = input('''Select the number of the task to edit 
        or 0 to return to menu:                                       ''')
            # check if input is a number
            if edit.isdigit() == False:
                print('Please enter a number')
                continue
            # cast input as int
            edit = int(edit)
            # if 0 return
            if edit == 0:
                return
            elif edit > task:
                print ('Task number errror please try again ')           
            # check if task is complete
            elif content[edit-1][-1] == 'Yes':
                print('Completed tasks cannot be edited')
                continue 
            # check if task is not assigned to this user only allow own tasks to be edited unless admin 
            elif content[edit-1][0] != users[pair]:
                print('You can only edit your own tasks')
                if users[pair] == 'admin':
                    print('Admin override')
                    break
                continue
            else:
                break
        
        # get user input to mark as complete or edit task
        action = input('Mark as complete or edit? c/e:                                        ').lower()
        # if mark as complete change 'No' to 'Yes'
        if action == 'c':
            content[edit-1][-1] = 'Yes'
        # else if edit
        elif action == 'e':
            while True:
                # get user input new user for task
                edit_user = input('Enter new user for task:                                              ')
                # check user not in list
                if edit_user not in users:
                    print('User not found')
                    continue
                else:
                    break
            while True:
                # get user input new task date 
                edit_date = input('Enter new task date EG:07 Nov 2022:                                   ')
                # if date is not 11 characters ask to re enter in correct format and continue
                if len(edit_date) != 11:
                    print('''Please enter date in format:                                          01 Jan 2023''')
                    continue
                # else format ok break
                else:
                    break
            
            # edit selected task in content
            content[edit-1][0] = edit_user
            content[edit-1][-2] = edit_date
        
        # for loop of content to get wanted format 
        for list in content:
            string = ', '.join(list)
            new_file += string
            new_file += '\n'
        new_file= new_file.strip()
        
        # with open open tasks.txt in write to overwrite file write new_file 
        with open('tasks.txt', 'w') as f:
            f.write(new_file)
        # reset task variable and return
        task = 0
        return

# define function to generate report
def gen_task_report():
    # get today
    today = get_today()

    # create variables
    tasks = 0
    comp_tasks = 0
    incomp_tasks = 0
    overdue = 0
    per_incomp = 0
    per_overdue = 0

    # with open tasks.txt in read
    with open('tasks.txt', 'r') as f:
        # for loop of f count tasks check if complete or not and if overdue
        for line in f:
            tasks += 1
            line1 = line.strip()
            line1 = line1.split(', ')
            due_date = datetime.strptime(line1[-2], '%d %b %Y').date()
            if line1[-1] == 'Yes':
                comp_tasks += 1
            elif line1[-1] == 'No':
                incomp_tasks += 1
                if due_date < today:
                    overdue += 1

    # if not 0 calc percent of incomplete and over 
    if incomp_tasks != 0:
        per_incomp = round((incomp_tasks / tasks) * 100, 2)
    if overdue != 0:
        per_overdue = round((overdue / incomp_tasks) * 100, 2)
    
    # create task_overview.txt with append write report
    with open('task_overview.txt', 'a') as g:
        g.write(f'''
Task Overview Report Generated on:  {today}
--------------------------------------------------
Total Number of Tasks:              {tasks}
--------------------------------------------------
Total Completed Tasks:              {comp_tasks}
--------------------------------------------------
Total Uncompleted Tasks:            {incomp_tasks}
--------------------------------------------------
Total Overdue Tasks:                {overdue}
--------------------------------------------------
Percentage Incomplete:              {per_incomp}%
--------------------------------------------------
Percentage of Incomplete
    that are Overdue:               {per_overdue}%
========================================================''')

# define function to generate user reports
def gen_user_report(users, passwords):
    # reset users
    users = []

    # call read users count tasks and get today 
    read_users(users, passwords)
    tasks = count_tasks()
    today = get_today()

    # create variables
    comp_tasks = 0
    incomp_tasks = 0
    per_task = 0
    per_comp = 0
    per_incomp = 0
    per_overdue = 0
    overdue = 0
    task = 0

    # create user_overview with append write report date total users and tasks
    with open('user_overview.txt', 'a')as f:
        f.write(f'''

         User Overview Report
      Report Generated on {today}
Total Users:                 {len(users)}
Total Tasks:                 {tasks}

''')

    # for loop of users
    for user in users:
        # open tasks.txt with read 
        with open('tasks.txt', 'r') as f:
            # for loop of lines counts users tasks complete, incomplete, and overdue
            for line in f:                
                line = line.strip()
                line = line.split(', ')
                due_date = datetime.strptime(line[-2], '%d %b %Y').date()
                if line[0] == user:
                    task += 1
                    if line[-1] == 'Yes':
                        comp_tasks += 1
                    elif line[-1] == 'No':
                        incomp_tasks += 1
                        if due_date < today:
                            overdue += 1

            # if variable not 0 calc percent 
            if task != 0:
                per_task = round((task / tasks) * 100, 2) 
            if comp_tasks != 0:
                per_comp = round((comp_tasks / task) * 100, 2)
            if incomp_tasks != 0:
                per_incomp = round((incomp_tasks / task) * 100, 2)
            if overdue != 0:                
                per_overdue = round((overdue / task) * 100, 2)

            # open user_overveiw as append and write which user and their stats
            with open('user_overview.txt', 'a') as g:
                g.write(f'''
        User:       {user}

Total Tasks:                      {task}
--------------------------------------------------
Percent of all tasks:             {per_task}%
--------------------------------------------------
Percent Completed:                {per_comp}%
--------------------------------------------------
Percent Incomplete:               {per_incomp}%
--------------------------------------------------
Percent Overdue:                  {per_overdue}%
========================================================
    ''')
    
        # reset variables and return 
        comp_tasks = 0
        incomp_tasks = 0
        per_task = 0
        per_comp = 0
        per_incomp = 0
        per_overdue = 0
        overdue = 0
        task = 0
    return

# define fuction to count tasks
def count_tasks():
    # create tasks
    tasks = 0
    # open tasks.txt to count tasks
    with open('tasks.txt', 'r') as f:
        # for loop to count tasks print with f string
        for line in f:
            tasks += 1
        return tasks

# define fuction to show stats
def show_stats(users, passwords):
    # reset users
    users = []
    # call read_users to re count users to catch new added users
    read_users(users, passwords)
    # call count tasks return num as task variable
    tasks = count_tasks()
    print(f'''
Number of Users:            {len(users)}
Number of Tasks:            {tasks}
        ''')
        # reset tasks and return
    tasks = 0
    return

#====Login Section====
# call read_users fuction to list users
read_users(users, passwords)

# welcome message
print('''========================================================
              Welcome to the task manager
                    Please Login
                  Enter 'e' to exit
========================================================''')

pair = login(users, passwords)

# personal welcome message if not e for exit
if pair != 'e':
    print(f'''========================================================
                     Welcome {users[pair]}''')

# while True
while True:
    # if to catch 'e' call to break out before menu
    if pair == 'e':
        print('''========================================================
                        Goodbye!!!
========================================================''')
        break
    # else if admin show admin menu
    elif users[pair] == 'admin':
        menu = admin_menu()

    # else show standard menu
    else:
        menu = stand_menu()
    
    # if input equals 'r'
    if menu == 'r':
        # check if user is admin
        if users[pair] == 'admin':
            reg_user(users, passwords)
            continue
        # else print not admin and continue
        else:
            print('''========================================================
                        ! ERROR !
            You need to be an admin to do this''')
            continue

    # else if menu input is 'a'
    elif menu == 'a':
        # call add_tasks and continue
        add_task(users, passwords)         
        continue

    # else if menu input 'va'
    elif menu == 'va':
        # call view_all and continue
        view_all()
        continue

    # else if menu input is 'vm'
    elif menu == 'vm':
        # call view_mine with 2 args and continue
        view_mine(users, pair)
        continue

    # else if 'g' and user is admin
    elif menu == 'g' and users[pair] == 'admin':
        # call task and user reports with 0 and 2 args respectively, print reports generated and continue
        gen_task_report()
        gen_user_report(users, passwords)
        print('                  Reports generated')
        continue

    # else if 'd' and user is admin
    elif menu == 'd' and users[pair] == 'admin':
        # check if one of the file exists both generated together so only need to check one
        if os.path.exists('user_overview.txt') == False:
                # if doesnt exist gen task and user report
                gen_task_report()
                gen_user_report(users, passwords)
        # open and print task overview
        with open('task_overview.txt', 'r') as f:
            for line in f:
                print (f'{line}')
        # open and print user overview
        with open('user_overview.txt', 'r') as g:
            for line in g:
                print (f'{line}')
        continue

    # else if menu input is 's' and user is admin
    # added the and in case normal user enters 's' they cannot access this feature
    elif menu == 's' and users[pair] == 'admin':
        show_stats(users, passwords)
        continue
    # else if menu is 'e' print goodbye and exit
    elif menu == 'e':
        print('''========================================================
                        Goodbye!!!
========================================================''')
        exit()
    # else print wrong input and continue to menu
    else:
        print('''========================================================
      You have made a wrong choice, Please Try again''')
        continue
