tasks = []

# Simple Todo App
# This is a simple command-line Todo application that allows users to add, view, and delete tasks.
# It uses a list to store tasks and provides a simple menu for user interaction.
# Could be improved by adding file storage or a database for persistent task management.

#Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added succesfully.")

#Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# Function to delete a task
def delete_task():
    if not tasks:
        print("No tasks available to delete.")
    else:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("Invalid task number.")

# Main function to run the Todo app
def main():
    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting Todo App.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()