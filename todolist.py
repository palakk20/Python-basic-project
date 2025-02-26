def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed!")
    else:
        print("Task not found!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def todo_list():
    tasks = []
    
    while True:
        print("\nTo-Do List:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Try again.")

todo_list()
