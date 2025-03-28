# todo.py
import sys

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Task '{task}' added.")

    def mark_done(self, task_number):
        if task_number < 1 or task_number > len(self.tasks):
            print("Invalid task number.")
            return
        self.tasks[task_number - 1]["done"] = True
        print(f"Task {task_number} marked as done.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['task']} - {status}")

def main():
    todo = Todo()
    while True:
        print("\n1. Add Task\n2. Mark Task Done\n3. Show Tasks\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.show_tasks()
            task_number = int(input("Enter task number to mark as done: "))
            todo.mark_done(task_number)
        elif choice == "3":
            todo.show_tasks()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()

