todo_list = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == "2":
        if not todo_list:
            print("No tasks.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
