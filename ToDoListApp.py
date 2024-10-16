# This is a simple To Do list 

tasks =[]

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")

def listTask():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")



def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter # to delete: "))
        if taskToDelete >= 0 and taskToDelete > len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed. ")

        else:
            print(f"Task #{taskToDelete} was not found.")     

    except:
        print("invalid input")

if __name__ == "__main__":
    ### create a loop to run the app
    print("Welcome to the To Do list app :) ")
    while True:
        print("\n")
        print("Please select oen of the following options")
        print("__________________________________________")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List a task")
        print("4. Quit")

        choice =input("Enter your choice: ")

        if(choice == "1"):
            addTask()

        elif(choice == "2"):
            deleteTask()

        elif(choice == "3"):
            listTask()

        elif(choice == "4"):
            break

        else:
            print('Invalid input. Please try again.')

    print("GoodBye! 👋👋") 
