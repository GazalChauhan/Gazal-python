# Displaying a menu
def display_menu():
    print("\n====== TO-DO LIST=====")
    print("1. add task")
    print("2. view task")
    print("3. mark as done")
    print("4. exit")

#adding tasks
def add_task(tasks):
    task = input("enter task description:")
    tasks.append(task)
    print("task added successfully!")

# viewing task
def view_tasks(tasks):
    print("\ntasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}.{task} - {status}")

#marking task as done
def mark_task_done(tasks):
    if not tasks:
        print("no task to mark as done")
        return
    
    view_tasks(tasks)
    #display tasks with indices
    index = int(input("enter task index to mark as done:")) - 1

    if 0 <= index <len(tasks):
        removed_task = tasks.pop(index)
        print(f"task'{removed_task}' marked as done and removed")
    else:
        print("invalid task index")

#main program logic
def main():
    tasks = [] #initialise an empty list to store tasks
    while True:
        display_menu()

        choice = input("enter your choice:")

        if choice =='1':
            add_task(tasks)
        elif choice =='2':
            view_tasks(tasks)
        elif choice =='3':
            mark_task_done(tasks)
        elif choice == '4':
            print("exitinf")
            break
        else:
            print("invalid choice")

if __name__=="__main__":
    main()

