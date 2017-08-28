# Python Exercise:
# STUDENT DATABASE MANAGEMENT SYSTEM, part 1

# Create a student database which stores the following information:
# student name, job, current Python level (for each student)

# The user will manage the database using the following commands:
#       add (to add a student to the database, issuing a warning if the student already exists)
#       delete (to delete a student from the database, issuing a warning if the student is not in the database)
#       print (to display information about the students, comprising tot numb of students)
#       average (to return average python level of all students)
#       exit (to exit the database)

student_db={}

def get_user_command():
    # this will take a user command and then call the dispatcher
    while True:
        user_input=input('Please insert your command <add>, <delete>, <print>, <average> or type <exit> to exit the database')
        user_input_split = user_input.split()
        if(user_input.find('exit')!=-1):
            return
        dispatcher(user_input_split)

def dispatcher(cmd_list_in):
    # takes a user command and then calls the corresponding function
    if cmd_list_in[0] == 'add':
        if (len(cmd_list_in))<4:
            print("ERROR: Add function must be followed by: <name>, <job>, <python level>")
        else:
            print ("calling add - it must be followed by <name> <job> <python level>") #call function
            add_user(cmd_list_in[1], cmd_list_in[2], cmd_list_in[3])
    elif cmd_list_in[0] == 'delete':
        print ("calling delete - it must be followed by <name>") # call function
        delete_user(cmd_list_in[1])
    elif cmd_list_in[0] == 'print':
        print ("calling print") # call function
        print_user(student_db)
    elif cmd_list_in[0]=='average':
        print ("calling average") # call function
        average_user(student_db)
    else:
        print ("ERROR: commands can only be <add>, <delete>, <print>, <average> or <exit>")

def add_user(name_in, job_in, python_exp_in):
    # the dictionary will have name of students as keys and tuples (job, python level) as values
    if name_in in student_db.keys():
        print('Sorry but this name already exists in the database')
    else:
        student_db[name_in] = (job_in, python_exp_in)
        print(name_in, 'has been added to the database')
    print("Your student database now looks as follows")
    print (student_db)
    return

def delete_user(name_in):
    if name_in not in student_db.keys():
        print('Sorry, this student is not present in the database')
    else:
        del student_db[name_in]
        print(name_in, 'has been deleted from student database')
    print("Your student database now looks as follows")
    print(student_db)
    return


def print_user(student_db):
    # number of students in the database
    student_numb=len(student_db)
    print('The number of the students in the database is: ', student_numb)

    # mix and max python level among students
    python_exp_list = []
    for v in student_db.values():
        python_exp_list.append(int(v[1]))
    min_python_lev=min(python_exp_list)
    max_python_lev=max(python_exp_list)
    print('The lowest python level among the students is: ', min_python_lev)
    print('The greatest python level among the students is: ', max_python_lev)

    # for all students Name: Job, python level: Value
    for k in student_db.keys():
        print (k, ':', student_db[k][0], ', python level:', student_db[k][1])


def average_user(student_db):
    # average level of python among the students
    python_exp_list = []
    for v in student_db.values():
        python_exp_list.append(int(v[1]))
    sum_pyth_exp=sum(python_exp_list)
    average_pl=sum_pyth_exp/len(python_exp_list)
    average_pl_r=round(average_pl,2)
    print('The average value of python level for all students in the db is: ', average_pl_r)


