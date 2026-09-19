tasks = []


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(i, task)


def remove_task(tasks):
    task = input("Enter a task to remove: ")

    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
    else:
        print("Task not found.")


while True:
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        remove_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")