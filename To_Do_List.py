def Todolist():
    tasks = []
    while True:
        print("What do you want to do?")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List All Tasks")
        print("4. Quit")
        print("Enter the Choice: ")
        choice = input()
        if choice == '1':
            task_name = input('Enter the name of the task: ')
            tasks.append(task_name)
            print(f"Task '{task_name}' added.")
        elif choice == '2':
            if len(tasks) == 0:
                print("No tasks to delete.")
            else:
                print("Tasks".center(40, "="))
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                print("".center(40, "="))
                task_no = input('Enter the task number to delete: ')
                if not task_no.isdigit() or int(task_no) < 1 or int(task_no) > len(tasks):
                    print("Invalid task number.")
                else:
                    deleted_task = tasks.pop(int(task_no) - 1)
                    print(f"Deleted Task: {deleted_task}")
        elif choice == '3':
            if len(tasks) == 0:
                print("No tasks to list.")
            else:
                print("Tasks".center(40, "="))
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                print("".center(40, "="))
        elif choice == '4':
            print("Thanks for using :)")
            break
        else:
            print("Invalid Choice! Try again.")

Todolist()
