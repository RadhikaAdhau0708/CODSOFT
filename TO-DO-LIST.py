class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
        
    def __str__(self):
        status = "RIGHT" if self.completed else "WRONG"
        return f"[{status}] {self.title}"
    
class ToDoApp:
    def __init__(self):
        self.tasks = []
        
    def show_menu(self):
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. Exit")
        
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
                
    def add_task(self):
        title = input("Enter task title: ")
        self.tasks.append(Task(title))
        print("Task added.")
        
    def update_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(self.tasks):
                new_title = input("Enter new title: ")
                self.tasks[num - 1].title = new_title
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    def mark_done(self):
        self.view_tasks()
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1].completed = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    def delete_task(self):
        self.view_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                deleted = self.tasks.pop(num - 1)
                print(f"Deleted task: {deleted.title}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-6): ")
            
            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.mark_done()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    app = ToDoApp()
    app.run()            
            