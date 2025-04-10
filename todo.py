todo_list = []

def show_menu():
    print("\n====== TO-DO LIST APP ======")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def show_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-4.")
