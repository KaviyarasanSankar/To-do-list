class ToDoItem:
    def _init_(self, task):
        self.task = task
        self.completed = False

    def _str_(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.task}"

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(ToDoItem(task))
        print("Task added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, item in enumerate(self.tasks, start=1):
            print(f"{idx}. {item}")

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task = new_task
            print("Task updated.")
        else:
            print("Invalid index.")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted.")
        else:
            print("Invalid index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)

        elif choice == '2':
            print("\nTo-Do List:")
            todo_list.view_tasks()

        elif choice == '3':
            index = int(input("Enter the index of the task to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)

        elif choice == '4':
            index = int(input("Enter the index of the task to complete: ")) - 1
            todo_list.complete_task(index)

        elif choice == '5':
            index = int(input("Enter the index of the task to delete: ")) - 1
            todo_list.delete_task(index)

        elif choice == '6':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
