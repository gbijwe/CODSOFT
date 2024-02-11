# A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists
import json

with open("data.json", 'r') as fp: 
    data = json.load(fp)

data['taskList'] = data['taskList']

def retrieveList(): 
    with open("data.json", 'r') as fp: 
        return json.load(fp)

def saveList(): 
    with open("data.json", 'w') as fp: 
        json.dump(data, fp, indent=2)

def addTask(): 
    print("Add Task ---------------------")
    task = str(input("Enter your task:  "))
    data['taskList'].append(task)

def completeTask(): 
    idx = int(input("Please enteer the task number completed: "))
    data['taskList'].pop(idx-1)

def deleteTask(): 
    idx = int(input("Please enteer the task number to delete: "))
    data['taskList'].pop(idx-1)

def displayTasks(): 
    print("\033[1m" + "\nDisplaying all tasks" + "\033[0m" +  " ----------------------------------\n")
    if len(data['taskList']) == 0: 
        print("\tno tasks")
        print("-------------------------------------------------------")
    else: 
        for index, x in enumerate(data['taskList']): 
            print("\t\x1B[3m" +f"Task #{index+1} : "+ x + "\x1B[0m")
    print("-------------------------------------------------------")

def welcome(): 
    print()
    print("\033[1m" + "Welcome to TODO" + "\033[0m")
    print("-------------------------------------------------------")
# Defining main function 
def main(): 
    while True: 

        print("\t\x1B[3m" + "1. Add a task" + "\x1B[0m")
        print("\t\x1B[3m" + "2. List all tasks" + "\x1B[0m")
        print("\t\x1B[3m" + "3. Delete a task" + "\x1B[0m")
        print("\t\x1B[3m" + "4. Complete a task" + "\x1B[0m")
        print("\t\x1B[3m" + "5. Exit TODO" + "\x1B[0m")

        print("-------------------------------------------------------")
        choice = int(input("Please select an operation to perform : "))

        match choice: 
            case 1: 
                addTask()
                saveList()
            case 2: 
                displayTasks()
            case 3: 
                displayTasks()
                deleteTask()
                saveList()
            case 4: 
                displayTasks()
                completeTask()
                saveList()
            case 5: 
                  print("\x1B[3m" + "\nExiting now. Thank you for using TODO :)" + "\x1B[0m")
                  saveList()
                  exit()
            case _: 
                print("-------------------------------------------------------")
                print("\033[1m" + "Select a valide choice: " + "\033[0m")
                print("-------------------------------------------------------")

                # main()


# Using the special variable  
# __name__ 
if __name__=="__main__": 
    welcome()
    retrieveList()
    main() 